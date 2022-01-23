int inorder[100000];
int postorder[100000];
int pos[100001];

void preorder(int ins, int ine, int posts, int poste)
{
	if (ins > ine || posts > poste)
		return;

	cout << postorder[poste] << ' ';
	int r = pos[postorder[poste]];

	preorder(ins, r - 1, posts, posts + r - ins - 1);
	preorder(r + 1, ine, posts + r - ins, poste - 1);
}
