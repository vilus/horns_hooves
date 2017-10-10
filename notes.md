- [ ] TODO: parametrize port in section proxy_pass nginx config
#
> when expose of containers ports need to configure firewall:
```sh
firewall-cmd --zone=public --add-port=5432/tcp --permanent
firewall-cmd --reload
```
> example cmdline of deploy "staging" via ansible:
```sh
docker run -it --rm -v ${HOME}/.ssh:/root/.ssh:ro -v $(pwd):/ansible -w /ansible ansible/centos7-ansible ansible-playbook -i inventories/staging site.yml
```
#
- [ ] TODO: create ssh keys for "staging"
- [ ] TODO: create docker-compose for rebuild (and push) images
- [ ] TODO: add volume for uploads to dj_back containers
- [ ] TODO: configure logging to stdout for docker settings of dj_back

