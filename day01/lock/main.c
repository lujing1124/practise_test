#include <stdio.h>
#include "digital_pwd.h"
#include <string.h>
int check_password(char pwd[20]){
    if(strlen(pwd) == 6){
        return 1;
    }
    return 0;
}

void delete_digital_pwd(){
    printf("请输入要删除的密码：\n");
    char pwd[20];
    scanf("%s",pwd);
    if(check_password(pwd)==0){
        printf("密码输入长度有误！\n");
        delete_digital_pwd();
    }
    if(!is_contain(pwd)){
        printf("系统中无此密码！\n");
        delete_digital_pwd();
    }
    delete_node(pwd);
}


void add_digital_pwd(){
    char pwd[20];
    scanf("%s",&pwd);
    if(is_contain(pwd)){
        printf("系统已经包含该密码，请更换！\n");
        add_digital_pwd();
    }
    if(!check_password(pwd)){
        printf("密码输入长度有误！\n");
        add_digital_pwd();
    }else{
        printf("请再次输入密码：\n");
        char comfirm_pwd[20];
        scanf("%s",&comfirm_pwd);
        if(!check_password(comfirm_pwd)){
            printf("密码输入长度有误！\n");
            add_digital_pwd();
        }

        if(strcmp(pwd,comfirm_pwd)){
            printf("两次密码输入不一致！请重新输入：\n");
            add_digital_pwd();
        } else{
            
            if(add_node(comfirm_pwd)){
                printf("添加成功！\n");
            }else{
                printf("内存不足！\n");
            }
            add_digital_pwd();
        }
    }
}

void digital_pwd_manager_ui(){
    printf("\n-------密码管理-------\n*1、添加密码\n*2、删除密码\n*3、删除所有密码\n*4、返回上一级\n");
    printf("请选择指令：");
    int command;
    scanf("%d",&command);
    switch(command){
        case 1:
            //pswd
            add_digital_pwd();
            break;
        case 2:
            delete_digital_pwd();
            break;
        case 3:
            //door manage
            break;
        case 4:
            //logout
            return;
        default:
            printf("请输入正确的指令！\n");
            digital_pwd_manager_ui();
            break;
    }
}

void adminUI(){
    printf("\n-------管理后台-------\n*1、密码管理\n*2、指纹管理\n*3、门禁管理\n*4、退出\n");
    printf("请选择指令：");
    int command;
    scanf("%d",&command);
    switch(command){
        case 1:
            //pswd
            digital_pwd_manager_ui();
            break;
        case 2:
            //finger manage
            break;
        case 3:
            //door manage
            break;
        case 4:
            //logout
            printf("系统退出中……\n");
            break;
        default:
            printf("请输入正确的指令！\n");
            adminUI();
            break;
    }

}

void welcomeUI(){
    printf("jenny 欢迎你！\n请输入管理员密码：");
    int password;
    int errorCount = 0;

    while(1){
        if(errorCount>=3){
            printf("密码错误输入已超过3次，请1分钟后再世！\n");
            return;
        }
        scanf("%d",&password);
        if(password == ADMIN_DEFAULT_PWD){
            // printf("");
            adminUI();
            break;
        } else {
            ++errorCount;
            printf("密码错误，请重新输入:\n");
        }
    }
    
}

int main(){
    welcomeUI();
    

    printf("");
    return 0;
}