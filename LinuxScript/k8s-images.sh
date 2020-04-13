#!/bin/bash
# download k8s 1.15.2 images
# get image-list by 'kubeadm config images list --kubernetes-version=v1.15.2'

images=(
kube-apiserver:v1.18.1
kube-controller-manager:v1.18.1
kube-scheduler:v1.18.1
kube-proxy:v1.18.1
pause:3.2
etcd:3.4.3-0
coredns:1.6.7
)

for imageName in ${images[@]};do
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
done
