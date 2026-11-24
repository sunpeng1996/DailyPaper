---
title: 'DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal
  Embeddings'
title_zh: DiLE：面向通用多模态Embedding的判别感知隐空间学习框架
authors:
- Ben Kang
- Junda Wang
- Yuxuan Yuan
- Hang Li
- Yuhan Liu
- Xin Chen
- Wanting Geng
- Tong Lin
- Pei Fu
- Dong Wang
affiliations:
- 大连理工大学
- 北京大学
- 小米集团
- 香港城市大学
arxiv_id: '2611.25419'
url: https://arxiv.org/abs/2611.25419
pdf_url: https://arxiv.org/pdf/2611.25419
published: '2026-11-18'
collected: '2026-11-24'
category: RecSys
direction: 多模态Embedding · 通用检索优化
tags:
- Multimodal Embedding
- LoRA
- Knowledge Distillation
- Hard Negative Mining
- Latent Learning
one_liner: 提出两阶段判别感知隐空间学习框架，大幅提升通用多模态Embedding的检索性能与推理效率
practical_value: '- 多模态商品/内容召回场景可直接复用TLSL设计：新增4个可学习隐查询+推理指令+辅助答案生成监督，无需显式生成推理链即可提升Embedding判别性，推理侧无额外开销

  - 多任务Embedding训练可复用SPEA架构：基于LoRA实现共享+私有专家，共享专家学习跨任务通用特征，私有专家适配不同检索任务（图文/视频/商详页检索）的特性，参数效率高

  - 难例蒸馏可借鉴OPHD方案：定期用当前学生快照刷新难例，用大模型重排器作为教师，反向KL对齐相似度分布的效果优于正向KL/JSD，能大幅提升易混淆样本（如相似商品）的区分度

  - 训练流程可直接复用两阶段范式：先做任务感知表征学习，再做判别性蒸馏，推理逻辑无需修改，可无缝替换业务现有多模态Embedding模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前基于MLLM的通用多模态Embedding语义理解能力强，但易丢失区分易混淆样本的关键证据（如同款不同色商品、存在空间关系差异的图文对），导致难例区分度低、检索准确率不足，且现有带显式推理的方案推理延迟高，难以落地。
### 方法关键点
- **Task-guided Latent Space Learning（TLSL）**：在输入序列后追加固定推理指令+4个可学习隐查询，对隐查询的最终隐态做平均池化得到检索向量；新增辅助答案生成监督，引导隐查询抓取任务相关的判别性信息
- **Shared-Private Expert Adaptation（SPEA）**：基于LoRA实现，共享专家学习跨任务通用知识，6个私有专家分别适配不同模态/检索任务的判别需求，兼顾知识复用与任务特性
- **On-Policy Hard-negative Distillation（OPHD）**：定期用当前学生快照检索难例，用冻结的Qwen3-VL-Reranker-8B输出细粒度相关性分布，用反向KL对齐学生的Embedding相似度分布与教师分布，仅当教师Top1为标注正例时计算蒸馏损失，避免错误监督
### 关键实验
在MMEB-V2（78个多模态检索任务）、MRMR（推理密集型多模态检索）、UVRB（16个视频检索任务）三个通用基准上均取得SOTA：
- 基于Qwen3-VL-2B的DiLE比同骨干Embed-RL高2.8%，吞吐量提升101倍
- 基于Qwen2-VL-2B的DiLE比同骨干PLUME高4.3%，吞吐量提升4倍
### 核心结论
无需显式生成推理链，通过隐空间任务引导+on-policy难例蒸馏即可同时兼顾多模态Embedding的判别性与推理效率。
