#include <stdio.h>
struct node{
	int data;
	struct node * next;
}; 

void revr(struct node * head){
	struct node* curr = head;
	struct node* prev = NULL;
	struct node* nex = NULL;	
	struct node* temp = (struct node * )malloc(sizeof(struct node));
	temp=head;
	while(temp!=NULL){
		printf("%d->%u\n",temp->data,temp);
		temp = temp->next;
	}
	printf("::::%u\n",curr);
	while(curr!=NULL){
		nex = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nex;
		printf("::::%u\n",nex);
	}
	head=prev;
	temp=head;
	while(temp!=NULL){
		printf("%d ",temp->data);
		temp = temp->next;
	}
	
}

int main(){
	int n,i,x;
	scanf("%d",&n);
	struct node* head = (struct node * )malloc(sizeof(struct node));
	printf("enter data: ");
	scanf("%d",&head->data);
	struct node* temp = (struct node * )malloc(sizeof(struct node));
	temp=head;
	for(i=1;i<n;i++){
		printf("enter data: ");
		scanf("%d",&x);
		struct node* neww = (struct node * )malloc(sizeof(struct node));
		neww->data=x;
		neww->next=NULL;
		temp->next=neww;
		temp= temp->next;		
	}
	temp->next = NULL;   
	revr(head);
}

