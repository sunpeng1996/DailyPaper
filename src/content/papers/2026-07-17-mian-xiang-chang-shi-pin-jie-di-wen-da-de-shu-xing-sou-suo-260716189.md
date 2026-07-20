---
title: 'Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video
  QA'
title_zh: 面向长视频接地问答的树形搜索自校正智能体框架
authors:
- Ce Zhang
- Ziyang Wang
- Yulu Pan
- Oluwatumininu Oguntola
- Pranav Wagh
- Qiyu Wu
- Hiromi Wakaki
- Mohit Bansal
- Gedas Bertasius
affiliations:
- University of North Carolina at Chapel Hill
- Sony
arxiv_id: '2607.16189'
url: https://arxiv.org/abs/2607.16189
pdf_url: https://arxiv.org/pdf/2607.16189
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 长视频理解 · Agent自校正搜索
tags:
- VideoQA
- Agent
- Temporal Grounding
- Hierarchical Search
- Reinforcement Learning
one_liner: 将长视频按语义边界构建为自适应时间树，用带显式回退的离散动作训练自校正Agent实现长视频接地问答
practical_value: '- 长序列内容（如用户全生命周期行为、长直播/商品讲解视频）的关键片段定位可复用自适应语义树构造方案，用内容相似度做非均匀分割，避免均匀采样的无效计算，提升检索效率

  - Agent设计中可加入显式回退/分支切换原语（如zoom_out、shift），替代单一的细化动作，解决探索过早收敛问题，可直接复用在搜索意图探索、多轮query改写、导购对话Agent等场景

  - Agent训练可复用「错误分支+回退恢复」的合成轨迹范式，仅对正确动作、纠错动作做损失回传，再结合RL调优，比仅用最优路径训练的模型在复杂场景下的纠错能力更强'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有长视频接地问答（Grounded LVQA）要求同时输出答案和对应的证据时间片段，现有Agent方法仅支持连续裁剪的粗到细探索，无显式回退机制，容易过早收敛陷入错误分支无法恢复；均匀采样长视频要么漏过关键证据要么超过输入上下文预算，急需更高效的结构化搜索方案。

### 方法关键点
- 自适应时间树构造：用CLIP计算相邻帧语义相似度，按内容变化点做非均匀分割，根节点对应全视频，叶节点为短于64s的语义连贯片段，树节点懒加载，仅构造访问过的节点子树，降低计算量
- 离散动作空间：设计4种可学习原语：zoom_in（下钻子节点）、zoom_out（回退父节点）、shift（切换同级节点）、answer（输出结果），将回退纠错从隐式行为转化为显式可训练动作
- 训练范式：先合成包含「错误分支探索+回退恢复」的轨迹做SFT，仅对正确动作、回退动作做损失回传，错误动作仅作为上下文不参与损失计算；再用GRPO做RL微调，奖励覆盖动作格式合规性、证据IoU、回答准确率三个维度

### 关键结果
在3个Grounded LVQA基准上：CG-Bench比最优Agent基线高+12.5 mIoU，Haystack-Ego4D高+7.4 T-F1；迁移到3个通用长视频QA基准，比最优基线最高提升+7.1准确率；每视频平均仅4.8轮搜索，处理328帧，比均匀采样384帧、Captioner-LLM方案450帧效率更高，60%的轨迹会用到回退动作，证明纠错机制有效。

> 最值得记住：结构化语义树+显式回退原语+错误轨迹训练，比单一连续探索动作更适合长序列稀疏目标搜索场景
