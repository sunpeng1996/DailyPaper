---
title: 'Safe Alone, Unsafe Together: Safeguarding Against Implicit Toxicity When Benign
  Images Combine'
title_zh: 单图安全组合有害：多图组合隐式毒性检测与防护方法
authors:
- Jiaxian Lv
- Shiyao Cui
- Yingkang Wang
- Guoxin Wu
- Qingling Zhang
- Minlie Huang
affiliations:
- The Conversational AI (CoAI) Group, DCST, Tsinghua University
arxiv_id: '2607.00576'
url: https://arxiv.org/abs/2607.00576
pdf_url: https://arxiv.org/pdf/2607.00576
published: '2026-07-01'
collected: '2026-07-04'
category: Multimodal
direction: 多模态内容安全 · 多图隐式毒性检测
tags:
- Multimodal Safety
- Content Moderation
- Multi-image Understanding
- Dataset Construction
- Knowledge Distillation
one_liner: 构建多图隐式毒性专用数据集，训练带推理能力的MiShield模型，实现优于商用服务的多图违规检测
practical_value: '- 电商UGC/商品详情页内容审核场景可复用多图联合语义建模思路，解决现有单图审核漏检组合式违规内容的问题

  - 标注数据稀缺的垂类检测任务可复用「自动生成标注数据集+渐进式蒸馏推理监督」训练范式，降低标注成本

  - 内容合规要求高的平台可直接参考MIIT的7类风险分类框架，优化现有内容审核的规则覆盖度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前社交、电商等平台多图内容成为主流传播形式，单图无害、组合后产生隐式有害语义的多图隐式毒性（MIIT）风险凸显，现有商用单图审核API因缺乏跨图语义理解能力，对这类风险漏检率极高。
### 方法关键点
1. 首次明确定义MIIT问题，梳理出三大核心检测挑战；
2. 搭建自动数据生成管线，构建覆盖7类典型风险的MIIT-dataset，解决该领域数据稀缺问题；
3. 提出MiShield模型，采用渐进式蒸馏推理监督训练，可同步输出安全判定结果及致害关联实体分析。
### 关键结果
MiShield-8B模型效果优于主流商用审核服务及更大参数规模的基线模型，具备落地可行性
