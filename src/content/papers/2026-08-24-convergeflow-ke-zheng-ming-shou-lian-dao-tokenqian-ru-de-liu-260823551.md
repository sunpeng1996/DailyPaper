---
title: 'ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings'
title_zh: ConvergeFlow：可证明收敛到Token嵌入的流式语言模型
authors:
- Na Li
- Yuchen Jiao
- Changxiao Cai
- Gen Li
affiliations:
- Chinese University of Hong Kong
- University of Michigan, Ann Arbor
arxiv_id: '2608.23551'
url: https://arxiv.org/abs/2608.23551
pdf_url: https://arxiv.org/pdf/2608.23551
published: '2026-08-24'
collected: '2026-08-25'
category: LLM
direction: 连续流式语言建模 · 收敛性证明
tags:
- Flow Matching
- Diffusion Language Model
- Token Embedding
- Convergence Guarantee
- Generative Model
one_liner: 提出可证明收敛到Token嵌入的连续流式语言模型，无需CE监督解码器即可直接生成有效Token
practical_value: '- 做生成式推荐/QueryRec的连续扩散生成时，可复用嵌入凸组合参数化+MSE训练的设计，省去CE监督的解码器环节，降低训练复杂度

  - 生成任务中需要调控质量-多样性 trade-off 时，可直接复用论文提出的三种自适应采样机制：自条件引导、迭代自条件精炼、无引导采样，通过调参快速匹配业务需求（比如广告文案生成兼顾通顺度和多样性）

  - 当业务场景需要并行生成文本（比如批量生成商品标题、推荐理由）时，可尝试连续流式LM替代自回归模型，兼顾生成速度和质量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有连续扩散/流式语言模型无法保证生成轨迹终止在有效token嵌入，必须依赖交叉熵（CE）监督的解码器做离散映射，违背了连续建模的设计初衷，也限制了性能上限。

### 方法关键点
- 数据预测器参数化为词表嵌入的凸组合，权重由可学习基础权重+高斯核计算得到，全程仅用流匹配诱导的MSE损失训练，无需任何CE监督
- 理论证明在温和条件下，生成流可概率收敛到有效token嵌入，最终仅用最近邻匹配或权重取max即可得到离散token，无需额外解码器
- 提出三种采样机制调控生成质量（Gen. PPL）和多样性（熵）的trade-off：自条件引导、迭代自条件精炼、无引导采样，支持时间自适应调度

### 关键实验
在OpenWebText数据集上，130M参数的ConvergeFlow在数据集熵5.44下Gen. PPL低至33.17，远优于同类连续流式LM（LangFlow 60.09、ELF 65.30），甚至优于同参数规模的自回归Transformer（35.90）。

**最值得记住的一句话**：连续流式语言模型只要参数设计合理，完全可以摆脱CE监督的解码器，同时实现比自回归模型更优的生成效率和质量。
