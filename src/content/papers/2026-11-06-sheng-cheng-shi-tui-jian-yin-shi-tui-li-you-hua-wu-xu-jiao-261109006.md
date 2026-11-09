---
title: 'Rethinking Latent Reasoning for Generative Recommendation: Beyond Teacher-Generated
  CoT and Recurrent Hidden-State Feedback'
title_zh: 生成式推荐隐式推理优化：无需教师CoT与循环隐状态反馈的PHiT方法
authors:
- Yiwen Chen
- Fuwei Zhang
- Zehao Chen
- Deqing Wang
- Hehan Li
- Peizhi Xu
- Hanmeng Liu
- Shuanglong Li
- Xin Pei
- Fuzhen Zhuang
affiliations:
- Beihang University
- Baidu
arxiv_id: '2611.09006'
url: https://arxiv.org/abs/2611.09006
pdf_url: https://arxiv.org/pdf/2611.09006
published: '2026-11-06'
collected: '2026-11-09'
category: GenRec
direction: 生成式推荐 · 隐式推理优化
tags:
- Generative Recommendation
- Chain-of-Thought
- Thought Token
- Semantic ID
- Supervised Fine-Tuning
one_liner: 提出历史引导的预填充思考令牌方案，无需教师CoT与循环推理实现生成式推荐SOTA
practical_value: '- 可直接复用CoT剪枝结论：生成式推荐的CoT中仅历史分析步骤有正向贡献，偏好、意图推理步骤反而降低推荐效果，做CoT蒸馏时可直接剪去冗余步骤，既降监督成本又提效果。

  - 工程兼容度极高：新增固定思考令牌直接插入输入序列，无需定制循环隐状态反馈逻辑，完全适配现有vLLM等LLM serving框架的KV cache、prefill流程，改造成本极低。

  - 低成本监督方案可落地：无需大模型为每条训练样本生成CoT，用SPLADE等稀疏编码器预编码全量商品元数据并缓存，聚合用户交互历史的语义得到监督信号，训练成本降低两个数量级，适配百万级以上电商商品库。

  - 训练trick复用：联合历史语义多标签分类（类平衡BCE损失）与SID预测损失做SFT即可提效，无需RL后处理阶段，落地门槛大幅降低。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式推荐的隐式推理存在两大落地痛点：一是依赖大模型生成每条样本的教师CoT作为监督，构造成本极高；二是循环隐状态反馈需要定制推理链路，无法兼容现有LLM serving生态的标准prefill、KV cache流程，工程落地难度大。

### 方法关键点
- 先完成CoT step级诊断：量化每个推理步骤对推荐准确率、CoT连贯度的贡献，发现仅历史分析步骤在两个维度均为正向贡献，后续偏好构造、意图推理步骤反而降低推荐准确率，验证历史语义是唯一有效监督信号。
- 提出PHiT框架：新增N个固定ID的思考令牌插入用户历史与目标Semantic ID (SID)之间，单轮causal prefill即可生成用户专属的思考令牌上下文状态，无需循环隐状态反馈。
- 低成本监督构造：用冻结的SPLADE编码器预编码全量商品元数据并缓存，聚合用户交互历史的商品语义得到Top-K关键词作为多标签监督，和SID预测损失联合做Supervised Fine-Tuning (SFT)，推理时直接丢弃辅助头，无额外 overhead。

### 关键实验结果
在Beauty、Instruments、Sports、Steam四个公开基准上，仅用SFT就超过所有基线，24个评测指标中22个显著优于带RL阶段的SOTA方案LASAR：Sports数据集HR@20提升21.7%、NDCG@20提升12.2%，Steam数据集HR@5提升11.2%；监督构造成本比教师CoT生成低77倍，13万训练样本仅需113秒完成目标构造，训练时间和无思考令牌的基线几乎一致。

**最值得记住的一句话：生成式推荐的隐式推理无需模拟复杂的人类偏好/意图推导过程，仅用观测到的历史语义做轻量监督就能实现效果和效率的双重最优。**
