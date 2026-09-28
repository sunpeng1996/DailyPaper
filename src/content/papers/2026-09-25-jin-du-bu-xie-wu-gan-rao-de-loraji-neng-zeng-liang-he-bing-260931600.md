---
title: New LoRA Skills Should Read but Never Write
title_zh: 仅读不写：无干扰的LoRA技能增量合并方法READ
authors:
- Zeyan Li
- Panqi Yang
- Qirong Guo
- Shengda Zhuo
- SIyuan Qiu
- Hu Xu
- Chun Li
- Jianfeng Xu
affiliations:
- Shanghai Jiao Tong University
- Xi'an Jiaotong University
- The Hong Kong University of Science and Technology (Guangzhou)
- Jinan University
arxiv_id: '2609.31600'
url: https://arxiv.org/abs/2609.31600
pdf_url: https://arxiv.org/pdf/2609.31600
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: 参数高效微调 · LoRA多技能合并
tags:
- LoRA
- model merging
- parameter efficient fine-tuning
- continual learning
- inference efficiency
one_liner: 提出仅读不写的LoRA增量合并机制READ，无旧技能损伤且合并后无额外推理成本
practical_value: '- 多业务场景LoRA合并可复用READ的「只读耦合+规范形式」设计，合并搜索query理解、商品文案生成、用户意图分类等不同场景LoRA时无互相干扰，无需重训旧技能

  - 工程上可复用READ的权重折叠机制，合并后的LoRA直接融入基座权重，无路由、无额外KV cache开销，适合大流量推荐/广告场景的LLM服务部署

  - 新增业务技能时仅需训练新技能对应的耦合矩阵行（单次仅训练万级参数），无需回溯旧业务数据，可大幅降低新功能上线成本与周期'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有独立训练的LoRA技能合并存在两大痛点：权重空间直接合并易产生技能干扰，甚至损伤原有效果；路由式多LoRA调度会带来额外推理开销，无法得到单一合并模型。持续新增技能时要么需要重训全量数据，要么无法兼容低延迟线上部署要求，无法满足业务场景多技能快速迭代、低成本落地的需求。
### 方法关键点
- 所有LoRA先转换为平衡规范形式：通过SVD/QR分解重写LoRA的A/B因子，完全保留原更新效果的同时消除因子坐标的随机自由度，保证不同LoRA的因子可对齐
- 只读耦合设计：新增LoRA时仅训练新技能对应的耦合矩阵行，禁止新技能向旧技能的输出子空间写入，从机制上保证旧技能不受新技能训练的影响
- 无开销折叠：合并后的整体LoRA更新可直接折叠进基座权重，无需路由、无需任务特定分支，推理延迟与原生基座模型完全一致
### 关键实验
在Llama-3.2-3B、Qwen3-4B两个主流开源模型，GLUE、SuperGLUE、Domain、BBH四个基准套件上和14种SOTA LoRA合并方法对比：平均比每个测试序列的最强基线高7.3个百分点，SuperGLUE上提升超20个点，Domain场景提升超7个点；92次增量合并中72次通过可靠性校验，旧技能平均损失不超过2个百分点；合并后模型推理延迟与原生基座差异小于1%，无额外存储或计算开销。
### 核心结论
当新技能需要和旧技能共享模型时，让新技能适应旧技能而非反过来，是避免旧技能损伤的核心。
