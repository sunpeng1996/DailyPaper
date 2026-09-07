---
title: 'ReRoom: Blending Virtual and Physical Contexts for In Situ Room Planning in
  Mixed Reality'
title_zh: ReRoom：融合虚实上下文的混合现实原位房间规划系统
authors:
- Hongliang Yang
- Yanjing Xu
- Anhang Zhang
- Hui Ye
- Pengfei Xu
affiliations:
- Shenzhen University
- Hong Kong Baptist University
arxiv_id: '2609.03596'
url: https://arxiv.org/abs/2609.03596
pdf_url: https://arxiv.org/pdf/2609.03596
published: '2026-09-03'
collected: '2026-09-07'
category: Agent
direction: Agent 空间布局生成与交互优化
tags:
- Mixed Reality
- Layout Generation
- Skill-guided Agent
- Context-aware Generation
- Human-Agent Interaction
one_liner: 提出融合虚实上下文的混合现实房间规划系统ReRoom，搭配技能引导Agent提升生成效率与体验
practical_value: '- 可复用技能引导Agent的设计思路：将家装、陈设等领域的专家规则转化为可执行校验算子，大幅减少生成式Agent的无效输出，降低推理成本

  - 虚实上下文绑定的生成逻辑可迁移至电商家装场景：用户上传房屋扫描/尺寸数据后，直接生成适配真实空间的家具推荐与组合布局方案，提升转化效率

  - 迭代生成的状态留存机制可复用：保留用户已确认的生成结果，后续生成仅调整未确认部分，降低用户交互成本，提升个性化匹配度'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有房间布局生成方案要么完全脱离真实物理空间编辑，要么对原位迭代优化的支持不足，无法匹配用户家装场景下逐次确认、按需调整的需求，生成效率与用户体验均存在短板。
### 方法关键点
1. 构建混合现实下与目标真实房间空间配准的虚拟代理，生成过程全程锚定物理上下文，支持用户通过直接操作、自然语言迭代调整布局，自动留存已确认的布局状态，后续生成基于已有确认结果迭代
2. 设计技能引导的布局Agent，将专业室内设计原则转化为标准化空间表征与可复用几何校验规则，平衡布局生成质量与效率
### 关键结果
评估显示ReRoom可针对非矩形房间生成高质量布局，其原位工作流相比同能力的离线VR工作流，用户房间规划体验提升显著
