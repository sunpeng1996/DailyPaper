---
title: 'Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for
  Pre-Trained LLMs'
title_zh: 自适应深度稀疏框架：面向预训练LLM的相似度驱动资源分配方法
authors:
- Yidu Wu
- Xiang Wang
- Kejie Zhao
- Zhangchi Wang
- Qinghai Guo
- Xiaoying Tang
affiliations:
- Southern University of Science and Technology
- Huawei Technologies Co., Ltd.
arxiv_id: '2607.21291'
url: https://arxiv.org/abs/2607.21291
pdf_url: https://arxiv.org/pdf/2607.21291
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: LLM推理优化 · 深度稀疏动态计算
tags:
- Efficient-LLM
- Depth-Sparsity
- Dynamic-Computation
- Inference-Acceleration
- Model-Compression
one_liner: 无需全量重训即可将预训练LLM转换为深度稀疏模型，实现更优的效率-效果权衡
practical_value: '- 可直接复用相似度驱动的层资源分配逻辑：部署业务侧LLM（如推荐文案生成、Agent决策大模型）时，先通过小批量校准数据计算每层输入输出隐向量相似度，动态分配各层token保留率，相同算力预算下可降低效果损失

  - 轻量路由+特征对齐训练方案可迁移：仅需新增轻量MLP路由层，用中间隐层对齐+输出分布对齐的损失做少量微调，无需修改Transformer主干，适配现有开源LLM
  checkpoint的快速稀疏化改造

  - 该方法可与量化、KV cache优化等现有部署优化方案叠加使用，进一步降低LLM在电商搜索推荐场景下的部署成本，提升单卡吞吐量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
预训练LLM推理成本随深度、序列长度线性/平方级增长，现有深度稀疏加速方案存在三大落地痛点：依赖任务特定微调或全量重训，预训练 checkpoint 适配成本高；固定/启发式token保留策略无法匹配不同层的表征变换强度，资源分配效率低；需大幅修改Transformer主干架构，落地门槛高，难以直接复用开源成熟模型。

### 方法关键点
- 相似度驱动层级资源分配：通过小批量校准集计算每层输入输出隐状态的余弦相似度，相似度越低代表该层表征变换贡献越大，分配更高的token保留率，在全局固定算力预算下实现资源动态倾斜
- 轻量无侵入路由设计：每层仅新增1个MLP轻量路由器，按保留率选择Top-K高价值token进入Transformer层计算，未选中token直接走残差通路，无需修改模型主干结构，训练时路由通路保持可微
- 特征保留对齐训练：联合优化两类对齐损失，一是中间隐层分布对齐（稀疏与稠密模型每层隐状态Softmax后的MSE），二是输出分布对齐（稠密模型到稀疏模型的KL散度），最小化稀疏化带来的表征偏移

### 关键实验
在GPT-NeoX-130M、Qwen2.5-0.5B/1.5B上测试，对比MoD、D-LLM、DLO等主流深度稀疏基线：80% token保留率下，GPT-NeoX在Wikitext103上PPL仅18.9（稠密基线17.9，MoD为21.6），FLOPs仅为稠密模型的0.787倍；Qwen2.5-0.5B在6项常识推理任务上平均准确率仅比稠密基线低2.6%，效果比MoD高4.7个百分点，FLOPs仅0.785倍。

### 核心结论
无需全量重训、仅做最小架构修改的相似度驱动稀疏化方案，是兼顾LLM部署效率、效果、落地成本的高性价比路径。
