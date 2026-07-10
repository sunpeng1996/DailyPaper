---
title: It Takes a MAESTRO To Prune Bad Experts
title_zh: MAESTRO：基于马尔可夫链的MoE大模型专家结构化剪枝框架
authors:
- Palaash Goel
- Ayush Maheshwari
- Tanmoy Chakraborty
affiliations:
- Indian Institute of Technology Delhi
- NVIDIA India
arxiv_id: '2607.08601'
url: https://arxiv.org/abs/2607.08601
pdf_url: https://arxiv.org/pdf/2607.08601
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: MoE大模型结构化剪枝优化
tags:
- MoE
- Structured Pruning
- Markov Chain
- LLM Compression
- LoRA
one_liner: 将MoE专家路由建模为遍历马尔可夫链，用稳态分布做全局剪枝，50%压缩下性能保留率超SOTA最高10.61%
practical_value: '- 业务侧用到MoE架构的LLM底座（生成式推荐文案、Agent推理、商品语义理解等）可直接复用MAESTRO剪枝流程，50%压缩率下仍保留92%+性能，大幅降低显存占用和部署成本

  - 剪枝后仅需轻量LoRA微调注意力层即可恢复性能，不需要重新训练专家和路由参数，工程落地成本极低，适合快速迭代的业务场景

  - 马尔可夫链建模全局依赖的思路可迁移到推荐系统的多塔模型、多通路召回模块的冗余剪枝，替代传统单通路重要性评估的局部偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
MoE大模型单token推理效率远高于同量级稠密模型，但全量专家需常驻显存，部署成本极高，无法落地到边缘、显存受限场景。现有剪枝方法多针对稠密Transformer设计，MoE专属剪枝方法也多依赖层内局部启发式规则评估专家重要性，忽略跨层路由的依赖关系，剪枝后性能损失大、跨任务泛化一致性差。
### 方法关键点
- 将token流经的（层，专家）序列建模为遍历马尔可夫链，在小校准语料上做自回归生成，统计层间专家的转移概率，构建全局转移矩阵
- 对转移矩阵做ε平滑加自环消除周期性，通过幂迭代求解稳态分布，稳态概率越低的专家全局贡献越小，优先剪除
- 每层均匀剪枝避免单层压缩过度导致性能瓶颈，剪枝后仅对注意力层做LoRA微调恢复性能，冻结专家和路由参数保留剪枝结构
### 关键结果
在GPT-OSS-20B、Qwen3-30B两个主流MoE模型上测试，覆盖17个benchmark跨5个领域（含安全、伦理维度），对比HC-SMoE、REAP、MOP等SOTA基线：25%压缩率下平均性能保留率达98.9%~99.4%，接近无损；50%压缩率下比最优基线高3.49%~3.6%，比HC-SMoE最高高10.61%，跨任务性能标准差比基线低40%以上。
### 核心结论
MoE剪枝不能只看单专家的局部激活频率，要基于全局路由信息流的稳态分布评估重要性，才能兼顾压缩率、性能保留和跨任务一致性。
