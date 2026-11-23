---
title: 'Model Carving: Training Transformers That Optimize Their Own Topology'
title_zh: 模型雕刻：训练可自主优化拓扑结构的Transformer
authors:
- Kaden Zheng
- Pratyusha Sharma
affiliations:
- Harvard University
- New York University
arxiv_id: '2611.27962'
url: https://arxiv.org/abs/2611.27962
pdf_url: https://arxiv.org/pdf/2611.27962
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 大模型训练 · 拓扑结构自动优化
tags:
- ModelCarving
- Transformer
- EfficientLLM
- TrainingOptimization
- StructuredPruning
one_liner: 单轮训练中联合优化Transformer权重与拓扑，产出更小更快质量无损的高效模型
practical_value: '- 训练端侧/低资源场景用的轻量化LLM时，可直接复用Model Carving方案：给子层加可学习门控自动裁剪无效结构，比先训大模型再蒸馏/剪枝省算力，质量还更高，适合电商端侧推荐的生成式文案、个性化query推荐等场景

  - 可借鉴「门控+动态计算压力」的设计思路，对推荐系统的多塔特征交互层加类似门控，训练中自动筛选有效特征通路，降低线上排序/召回模块的推理耗时

  - 裁剪后的模型无需存储无效Attention子层的KV cache，该结论可直接用于优化LLM推理部署，在电商智能客服、Agent推理等场景下最高可提1.6倍解码速度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统Transformer采用固定同质化层拓扑训练，架构设计与训练流程完全分离，往往存在大量冗余计算；主流轻量化方案需先训练大模型再剪枝/蒸馏，算力浪费严重且最终效果受限，亟需在单轮训练中同时优化权重与拓扑的高效方案。
### 方法关键点
- 初始化过参数化Transformer，每个Attention/MLP子层输出增加非负可学习门控，额外引入层间全连接可学习通路，门控初始值设为0.1预留裁剪空间
- 训练目标动态加入子层计算压力项：基于实时学习曲线估算子层计算成本对应的损失收益，当子层贡献低于压力时门控自动衰减至0
- 每300轮迭代统一裁去门控为0的子层，释放的算力可用于增加训练token，门控与权重在同一训练流中联合优化，无需额外NAS或后处理步骤
### 关键结果
在140M~2.7B参数量标准Transformer、140M~1.3B循环Transformer上验证，对比同训练算力全层模型、同推理算力浅层模型、剪枝/蒸馏同尺寸模型：
- 相同训练算力下，雕刻模型验证损失更低，全层模型需最多1.7倍训练算力才能追平效果
- 雕刻模型推理FLOP最高降34%，解码速度最高提1.61倍，KV cache最高省31%，下游CORE-22得分全面优于同尺寸剪枝/蒸馏模型
- 效果增益随模型规模扩大而提升，循环Transformer系列的优化收益显著高于标准Transformer
### 核心结论
每个大Transformer内部都隐含着一个更小、更快、效果更好的小模型，无需事后压缩，在训练过程中即可直接雕刻得到。
