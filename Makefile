.PHONY: fetch-master merge-master push-master update-posts publish

# Fetch latest changes from master branch
fetch-master:
	@echo "Fetching latest from master..."
	git fetch origin master:master

# Merge master into current branch
merge-master:
	@echo "Merging master into current branch..."
	git merge master || true

# Push current branch to master
push-master:
	@echo "Pushing current branch to master..."
	git push origin HEAD:master

# Update posts.json with published posts
update-posts:
	@echo "Updating blog/posts.json with published posts..."
	python3 update_posts.py

# Combined command: fetch from master, merge, update posts, and push to master
publish: fetch-master merge-master update-posts push-master
	@echo "Publish workflow completed!"
