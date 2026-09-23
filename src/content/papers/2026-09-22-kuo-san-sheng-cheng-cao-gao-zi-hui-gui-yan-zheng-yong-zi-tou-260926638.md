---
title: 'Diffusion Drafts, AR Verifies: Accelerating Document OCR with Self-Speculative
  Decoding'
title_zh: 扩散生成草稿+自回归验证：用自投机解码加速文档OCR
authors:
- Dohyun Kim
- Sungjun Han
- Hyungguk Kim
- Yusik Kim
- Jamin Shin
- Paul Hongsuck Seo
- Hongjoon Ahn
affiliations:
- Trillion Labs
- Korea University
- Seoul National University
arxiv_id: '2609.26638'
url: https://arxiv.org/abs/2609.26638
pdf_url: https://arxiv.org/pdf/2609.26638
published: '2026-09-22'
collected: '2026-09-23'
category: Multimodal
direction: 多模态OCR · 自投机解码推理加速
tags:
- OCR
- Speculative Decoding
- Diffusion Model
- Autoregressive Decoding
- Multimodal LLM
one_liner: 提出参数共享的扩散+AR联合OCR模型，通过自投机解码实现推理加速且精度损失极小
practical_value: '- 自投机解码的参数共享思路可迁移到GenRec的LLM推理加速场景，无需额外部署小draft模型即可实现多token并行生成，降低部署成本

  - 多模态任务中diffusion并行草稿+AR验证的架构，可复用在电商商品图文理解、凭证OCR等低延迟高准确率要求的场景

  - 用GRPO在AR路径优化共享参数的方法，可借鉴到生成式推荐的RLHF流程，规避扩散模型轨迹似然估计的复杂计算'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
自回归OCR多模态模型逐token顺序解码推理延迟高，难以满足大规模部署的吞吐要求；扩散式并行OCR生成因缺少相邻token上下文约束，直接输出易引入错误，现有投机解码方案需独立部署小draft模型，部署成本高。
### 方法关键点
提出GravityOCR，采用参数共享的AR块-扩散联合架构，同时训练并行草稿生成、因果AR验证两个路径：每轮扩散生成多token草稿后，经AR路径校验再提交有效token；AR路径支持引入序列/结构级OCR reward做GRPO训练，无需计算扩散轨迹似然即可更新共享的草稿生成参数。
### 关键结果
- OmniDocBench v1.6总分达95.16，仅比原版GLM-OCR低0.32分
- SGLang部署下平均每轮前向生成9.7个token，区域裁剪场景解码速度是纯AR解码的3.94倍，端到端页面处理速度提升1.32倍
