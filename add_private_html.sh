
# Add a private_html directory and redirect for the specified user
# This script must be run as superuser
#   e.g. usage:  sudo sh add_private_html.sh researcher
#
# This script assumes that we are using a GVL image with a pre-configured config file.
# This is usually achieved by running configure_nginx.sh first.

# Clare Sloggett, VLSCI, University of Melbourne
# Authored as part of the Genomics Virtual Laboratory project


conf_file="/usr/nginx/conf/private_html.conf"
username=$1
redirect="/private/"$username"/"

if [ -z "$1" ]; then
    echo "Require username on command line"
    exit 1
fi

sudo su $username -c 'mkdir ~/private_html'
sudo su $username -c 'chmod 755 ~/private_html'

# Check if this user already exists in conf file

if [ $(grep $redirect $conf_file | wc -l) != '0' ]; then
    echo "User "$username" appears to already have a redirect in "$conf_file"; aborting."
    exit 1
fi

# Add redirect

cat >> $conf_file << END
location $redirect {
     auth_pam    "Private HTML";
     auth_pam_service_name   "nginx";
     alias /home/$username/private_html/;
}
END

/usr/nginx/sbin/nginx -s reload
