---
title: 'From Symbolic Perception to Logical Deduction: A Framework for Guiding Language
  Models in Geometric Reasoning'
title_zh: 从符号感知到逻辑演绎：引导大模型实现几何推理的框架
authors:
- Weichen Dai
- Rafael Medeiros Cabral
- Ziyi Shou
- Yan Cao
- Xin Shen
- Dongcai Lu
- Yi Zhou
affiliations:
- University of Science and Technology of China
arxiv_id: '2609.10335'
url: https://arxiv.org/abs/2609.10335
pdf_url: https://arxiv.org/pdf/2609.10335
published: '2026-09-09'
collected: '2026-09-10'
category: Reasoning
direction: 大语言模型 · 符号逻辑推理
tags:
- LLM
- Symbolic Reasoning
- Geometric Reasoning
- Multi-modal Parsing
- Benchmark
one_liner: 提出纯LLM结合几何解析器与符号求解器的推理框架，性能比肩Gemini 2.5 Pro
practical_value: '- 多模态Agent任务可参考「视觉转符号+LLM推理」解耦架构，既降低大模型幻觉，又提升推理过程可解释性，可复用到电商商品图属性解析、合规校验等场景

  - 强逻辑类业务（如电商满减计算、优惠券规则核验）可借鉴外挂领域专属符号求解器的设计，替代纯端到端大模型方案，大幅降低推理算力成本

  - 业务效果基准测试可参考其构造全新真实场景数据集的思路，避免模型拟合现有公开基准的偏差，更准确反映线上真实表现'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
平面几何推理需要同时具备视觉感知与数学逻辑能力，现有多模态大模型（LMM）方案算力开销大、推理过程黑盒不可解释，纯符号推理系统又存在信息损失、规则适配性差的问题。
### 方法关键点
1. 采用纯LLM+外挂专用模块架构，无需依赖端到端多模态大模型
2. 接入Geometric Vision Parser将几何图转换为结构化符号表达，避免视觉信息解析误差
3. 搭配Symbolic Solver执行形式化逻辑推导，从根源减少推理幻觉
4. 构造2025年中国中考几何题基准数据集，保障测试数据新颖性，覆盖深度演绎能力验证
### 关键结果
推理性能与Gemini 2.5 Pro相当，输出的解题过程更清晰，更符合人类推理逻辑
