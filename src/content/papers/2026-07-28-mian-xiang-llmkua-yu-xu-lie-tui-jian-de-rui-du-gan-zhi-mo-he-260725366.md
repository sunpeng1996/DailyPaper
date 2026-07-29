---
title: Sharpness-aware Model Merging with Salience Recovery for LLM-based Cross-Domain
  Sequential Recommendation
title_zh: 面向LLM跨域序列推荐的锐度感知模型融合与显著性恢复方法
authors:
- Huwei Ji
- Jiajie Su
- Yuyuan Li
- Xiaohua Feng
- Chaochao Chen
affiliations:
- Zhejiang University
- Hangzhou Dianzi University
arxiv_id: '2607.25366'
url: https://arxiv.org/abs/2607.25366
pdf_url: https://arxiv.org/pdf/2607.25366
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 跨域模型融合优化
tags:
- Cross-Domain Recommendation
- Model Merging
- LoRA
- LLM4Rec
- Sequential Recommendation
one_liner: 提出SharpRec框架解决LLM跨域序列推荐模型融合的知识冲突与性能饱和瓶颈
practical_value: '- 单域LoRA微调阶段可直接复用SGA模块：加入锐度感知梯度扰动引导模型收敛到平坦极小值，无需修改模型结构即可降低跨域融合时的参数干涉，避免异质域负迁移

  - 多域LoRA线性融合后可接入PSA模块：通过小高斯噪声+自定义非线性激活重构参数为重尾分布，恢复被平均掉的域特异性特征，解决3~4个源域后性能饱和的问题

  - 低用户重叠跨域场景可直接复用整套框架：无需依赖大量重叠用户做特征对齐，仅通过参数空间几何对齐即可实现知识迁移，适配电商多业务线（服饰/美妆/家居等）跨域推荐需求

  - 超参数可直接参考论文最优区间：SGA扰动半径ρ取0.001~0.05，PSA激活因子γ取0.94~0.98，噪声σ_g取1e-6~1e-4，无需大量调参即可获得稳定收益'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于模型融合的LLM跨域序列推荐方案存在两大核心瓶颈：一是异质域（如运动/玩具）融合易出现参数干涉，导致负迁移，性能甚至低于单域基线；二是多域融合时性能快速饱和，接入3~4个源域后收益趋近于0，根源是参数层面几何不兼容、线性融合导致的统计均质化，域特异性显著参数被平均稀释。

### 方法关键点
- **Sharpness-aware Geometric Alignment (SGA)**：单域LoRA微调阶段加入自适应梯度扰动，引导模型收敛到平坦极小值，让不同域的LoRA参数处于连通的低损失域，从根源减少跨域参数冲突
- **Preference Salience Activation (PSA)**：线性融合多域LoRA后，先注入小范围高斯噪声打散均质化参数，再通过自定义非线性激活函数重构参数分布为带重尾的形式，重新激活被稀释的显著偏好信号，突破性能上限

### 关键实验结果
基于Amazon 2023的7个域数据集，对比11个SOTA基线（含传统CDSR、LLM4CDSR、WeaveRec等）：双域场景下NDCG@5比最优基线最高提升22.21%；7源域融合时NDCG@5比WeaveRec最高提升55.7%，源域数量增加时性能持续上升无饱和；用户重叠率低至20%时性能仅下降2%以内，远优于依赖重叠用户的传统方法。

### 核心结论
LLM跨域推荐模型融合的效果瓶颈，本质是参数的几何兼容性与分布特性问题，而非域知识本身的冲突
