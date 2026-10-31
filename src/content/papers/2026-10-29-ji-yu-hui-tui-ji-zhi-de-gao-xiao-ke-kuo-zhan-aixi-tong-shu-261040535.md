---
title: Efficient Scalable Oversight via Rewinding
title_zh: 基于回退机制的高效可扩展AI系统输出核验方法
authors:
- Ziyi Guan
- Yael Tauman Kalai
- Ron Rothblum
- Zoe Xi
affiliations:
- MIT
- Succinct
arxiv_id: '2610.40535'
url: https://arxiv.org/abs/2610.40535
pdf_url: https://arxiv.org/pdf/2610.40535
published: '2026-10-29'
collected: '2026-10-31'
category: Eval
direction: 大模型输出核验 · 可回退交互式证明
tags:
- Scalable Oversight
- Interactive Proof
- LLM Alignment
- Trustworthy AI
- Model Verification
one_liner: 提出可回退交互式证明RIP，无需预设诚实证明方，大幅降低大模型输出核验的计算成本
practical_value: '- 电商大模型推荐/Agent生成营销文案的核验场景，可复用RIP的状态快照回退机制，在可控运行环境下降低强模型输出的校验成本

  - 对鲁棒性要求高的广告审核、推荐排序类计算任务，可直接复用RIP的无密码学高效验证框架，无需预设诚实模型假设

  - 部署在可信硬件/云虚拟机的导购Agent系统，可基于状态快照做中间步骤回溯校验，提升生成结果的可信度'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有可扩展监督方案存在明显缺陷：基于辩论的方案高效但需预设至少一个诚实证明方，可靠性不足；无需诚实假设的方案则计算成本极高，难以落地到大模型输出核验场景。
### 方法关键点
1. 提出可回退交互式证明（RIP）框架，利用AI模型运行时可保存状态快照的特性，验证方可将证明方回退到交互任意历史节点重新核验
2. 针对小比例Oracle回答变化下输出鲁棒的计算任务，构造无密码学依赖的相对化RIP协议
### 关键结果
- 诚实证明方运行时间与原始计算线性相关，验证方经一次性预处理后运行时间接近输入长度线性（远小于计算本身耗时）
- MNIST实验中RIP速度优于现有已部署的最优证明系统
