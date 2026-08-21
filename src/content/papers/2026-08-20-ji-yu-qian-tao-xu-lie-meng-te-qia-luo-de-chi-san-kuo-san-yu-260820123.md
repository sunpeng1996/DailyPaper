---
title: Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo
title_zh: 基于嵌套序列蒙特卡洛的离散扩散语言模型推理时控制
authors:
- Lohithsai Yadala Chanchu
- Hany Abdulsamad
- Christian A. Naesseth
affiliations:
- University of Amsterdam
arxiv_id: '2608.20123'
url: https://arxiv.org/abs/2608.20123
pdf_url: https://arxiv.org/pdf/2608.20123
published: '2026-08-20'
collected: '2026-08-21'
category: LLM
direction: 大语言模型 · 推理时奖励对齐控制
tags:
- Discrete Diffusion
- Sequential Monte Carlo
- Inference-time Control
- Reward Alignment
- Text Generation
one_liner: 提出两种无偏嵌套SMC方法，无需重训练即可提升离散扩散生成的序列级奖励对齐效果
practical_value: '- 生成式推荐/电商文案生成场景可直接复用FA-NSMC，推理时对齐点击率、合规性等业务目标，无需重训练大模型，大幅降低对齐迭代成本

  - 算力分配上优先提升外层粒子数N，其次调整x0重建数K，内层候选数M≥8后收益饱和，适合业务侧受限算力下的参数调优

  - 长序列生成场景（比如商品详情页长文案、多轮Agent对话控制）优先选FA-NSMC，长奖励窗口下的目标达成率比普通SMC高60%以上

  - 黑盒奖励模型适配场景可复用x0重建近似中间奖励电位的方法，无需梯度回传即可实现任意离散生成任务的奖励引导'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
离散扩散语言模型（DDLM）可融合双向上下文生成全局一致性更高的文本，但其预训练输出无法天然对齐安全、业务目标。训练时对齐方法（如RLHF）算力成本高、易发生模式坍缩，且模型与单一奖励函数深度绑定；现有推理时无梯度对齐方法存在明显缺陷：best-of-n对稀有高奖励样本挖掘效率极低，bootstrap SMC存在严重的权重退化问题，亟需更高效的推理时控制方案。

### 方法关键点
- 提出两种无偏嵌套SMC算法（NSMC、FA-NSMC），修正了前人嵌套SMC实现的权重计算偏差，无限粒子极限下仍能无偏对准奖励倾斜分布
- NSMC为每个外层粒子运行内层SMC，基于多候选样本估计最优提议分布与归一化常数，解决传统SMC提议分布与奖励无关的问题
- FA-NSMC进一步将未来奖励估计纳入父粒子重采样阶段，提升粒子多样性，更适配长序列、高奖励不确定性场景
- 采用多步x0重建近似中间预期奖励电位，可适配任意黑盒奖励模型，无需梯度回传

### 关键结果
基于OpenWebText预训练的MDLM离散扩散模型，在毒性引导、流畅度引导任务上对比best-of-n、bootstrap SMC基线：同算力下FA-NSMC的毒性生成率达0.40，较bootstrap SMC提升60%、较best-of-n提升17倍，同时PPL降低13.7%；300token长奖励窗口下FA-NSMC的毒性率达0.47，较普通SMC提升62%；性能随外层粒子数N提升最显著，内层候选数M≥8后收益饱和。

**最值得记住的结论**：无梯度离散生成推理对齐场景下，FA-NSMC的性价比远超best-of-n与普通SMC，算力优先分配给外层粒子可获得最大收益。
