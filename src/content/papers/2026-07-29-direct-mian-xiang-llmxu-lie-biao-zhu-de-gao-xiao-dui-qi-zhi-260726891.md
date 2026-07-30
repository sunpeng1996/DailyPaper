---
title: 'DIRECT: Direct Decoding for Efficient and Aligned Sequence Labeling with Large
  Language Models'
title_zh: DIRECT：面向LLM序列标注的高效对齐直接解码框架
authors:
- Yilei Wang
- Jiaxin Gan
- Kexuan Zhang
- Ling Li
- Wentao Zhang
- Peichao Lai
affiliations:
- Fuzhou University
- Peking University
arxiv_id: '2607.26891'
url: https://arxiv.org/abs/2607.26891
pdf_url: https://arxiv.org/pdf/2607.26891
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: 大模型序列标注 · 训练对齐与推理加速
tags:
- Sequence Labeling
- DPO
- KV Cache
- Inference Acceleration
- Low-resource Learning
one_liner: 结合DPO训练对齐与KV缓存模板填充推理，实现LLM序列标注效果与效率双升
practical_value: '- 电商商品标题实体抽取、用户query意图识别等序列标注任务可直接复用训练范式：SFT后加入DPO训练，构造偏好对时选取BLEU高但F1低的输出为负样本，无需大量标注即可提升领域对齐度

  - 固定格式输出类任务（如标签生成、属性打标）可直接迁移推理优化技巧：仅让模型生成可变标签token，其余固定内容预填充KV缓存复用，实测推理速度最高提升9倍，显著降低部署成本

  - 垂直领域低资源标注场景（如细分品类属性打标）可参考低资源训练配置：仅用250条标注数据即可达到接近SOTA的效果，大幅减少数据标注成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于LLM的序列标注任务（如NER、词性标注）存在两大落地痛点：一是领域对齐不足，仅靠SFT和指令约束无法保证输出严格符合业务要求的格式和规则，垂直场景准确率低；二是推理效率差，传统自回归解码存在大量冗余计算，无法满足高吞吐量的业务需求（如电商实时query实体识别、海量商品属性打标）。
### 方法关键点
- 训练侧：SFT后新增DPO优化，构造偏好对时选择BLEU得分高但实体匹配F1低的输出作为负样本，真值作为正样本，强化模型对任务格式和标注规则的对齐
- 推理侧：采用受控解码机制，强制输出固定格式，仅允许模型从预定义标签候选集中选取token，避免无效生成
- 效率优化：已生成的固定前缀内容（模板符号、已输出的词和标签）提前预填充KV缓存，每次推理仅需生成当前词对应的标签token，消除冗余注意力计算
### 关键实验
在8个公开数据集（含淘宝、微博等中文电商/社交场景NER数据集）上对比InstructUIE、GoLLIE、GNER等SOTA基线，低资源设置下（训练样本量250/500/1000条），平均F1最高提升14.72%；推理速度最高达到基线的9倍，单L40 GPU上10条平均192token的样本仅需32.86s完成推理。
> 值得记住：对固定格式输出的序列类任务，「训练侧DPO对齐+推理侧约束解码+KV缓存复用」的组合是兼顾效果和落地效率的最优范式
