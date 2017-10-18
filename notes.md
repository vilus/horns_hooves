- [ ] TODO: parametrize port in section proxy_pass nginx config
#
> when expose of containers ports need to configure firewall:
```sh
firewall-cmd --zone=public --add-port=5432/tcp --permanent
firewall-cmd --reload
```
> example cmdline of deploy "staging" via ansible:
```sh
cd deploy
docker run -it --rm -v ${HOME}/.ssh:/root/.ssh:ro -v $(pwd):/ansible -w /ansible ansible/centos7-ansible ansible-playbook -i inventories/staging site.yml
```
#
- [ ] TODO: create ssh keys for "staging"
- [ ] TODO: add volume for uploads to dj_back containers!
- [ ] TODO: for deploy via ansible, in section upstream backends of nginx conf need to include file with adresses
- [ ] TODO: fix warning about deprecated "docker" in ansible staff
- [ ] TODO: move all definition vars in ansible playbooks to inventories/*/group_vars/all
- [ ] TODO: add CRUD via Django Rest Framework
- [ ] TODO: add history of goods modification

> work via docker:
```bash
./.venv/bin/docker-compose build
./.venv/bin/docker-compose up -d
# empty db, without users
./.venv/bin/docker-compose exec backend bash
python manage.py createsuperuser
# go to http://server_ip:/admin and add category, other users and etc
./.venv/bin/docker-compose down -v
# --
# for run in dev mode (w/ django dev server, load precreated fixtures to db)
./.venv/bin/docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```
