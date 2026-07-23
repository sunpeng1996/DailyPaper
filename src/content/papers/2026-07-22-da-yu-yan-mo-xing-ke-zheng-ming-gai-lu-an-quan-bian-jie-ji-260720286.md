---
title: Sound Probabilistic Safety Bounds for Large Language Models
title_zh: 大语言模型可证明概率安全边界计算框架
authors:
- Mahdi Nazeri
- Anne-Kathrin Schmuck
- Sadegh Soudjani
- Alessandro Abate
affiliations:
- University of Oxford Department of Computer Science
- Max Planck Institute for Software Systems
- University of Birmingham School of Computer Science
arxiv_id: '2607.20286'
url: https://arxiv.org/abs/2607.20286
pdf_url: https://arxiv.org/pdf/2607.20286
published: '2026-07-22'
collected: '2026-07-23'
category: Eval
direction: LLM安全评估 · 概率边界认证
tags:
- LLM Safety
- PAC Bound
- Latent Space
- Safety Evaluation
- Probabilistic Verification
one_liner: 提出基于隐空间特征和Clopper-Pearson区间的LLM有害输出概率严谨可证明下界计算框架
practical_value: '- 可复用隐空间分支优先探索的思路，高效评估生成式推荐/Agent回答的有害内容概率，替代全量采样降低算力成本

  - 电商场景下LLM生成商品文案/客服回复的安全审核可引入Clopper-Pearson PAC区间，获得统计可证明的有害率下界，满足合规要求

  - 生成式推荐系统上线前的安全评测可复用该框架，针对极低概率的违规输出场景获得严谨的风险量化指标'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM对齐技术仅能降低有害输出频率，无法提供可证明的安全保障，极低概率有害输出的全量采样评估成本极高，无法满足高风险场景的合规与风险量化需求。
### 方法关键点
1. 首次将Clopper-Pearson置信区间应用于LLM有害输出概率计算，获得具备PAC保证的概率边界
2. 提出基于隐空间特征的自回归生成树分支优先探索算法，优先排查更可能生成有害内容的生成路径，大幅提升低概率有害场景的评估效率
3. 输出的有害概率下界经过形式化证明，严格小于真实有害概率，结果具备严谨性
### 关键结果
在SOTA LLM上可稳定计算出有统计意义的有害率非平凡下界，即使真实有害概率极低的场景下也能高效得到可靠结果，首次支撑LLM的统计安全认证。
