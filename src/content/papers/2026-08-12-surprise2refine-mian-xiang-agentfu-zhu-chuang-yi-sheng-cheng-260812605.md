---
title: 'Surprise2Refine: Axis-Centered Exploration-To-Refinement for Agent-Assisted
  Creative Scaffolding'
title_zh: Surprise2Refine：面向Agent辅助创意生成的轴中心式探索到精细化工作流
authors:
- Yuzhe You
- Gromit Yeuk-Yin Chan
- Shunan Guo
- Anlan Zhang
- Eunyee Koh
- Jian Zhao
- Tongyu Zhou
affiliations:
- University of Waterloo
- Adobe Research
arxiv_id: '2608.12605'
url: https://arxiv.org/abs/2608.12605
pdf_url: https://arxiv.org/pdf/2608.12605
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: Agent辅助创意生成 · 人机协同交互
tags:
- Human-AI Collaboration
- Creative Agent
- Interaction Design
- Design Space Exploration
- Agent-Assisted Creation
one_liner: 提出基于可配置概念轴的动态网格工作流，适配创意设计从发散探索到收敛优化的全阶段需求
practical_value: '- 电商创意生成类Agent（如商品海报、营销文案生成工具）可复用轴中心动态网格设计，让用户自定义变异维度（如风格/构图/配色轴），降低prompt工程成本，提升生成可控性

  - 生成式推荐系统可复用探索-优化阶段适配逻辑：召回阶段输出匹配用户身份的惊喜候选，用户选中后进入精细化阶段，支持同款局部维度变异（如同款不同色/不同版型）的平滑探索

  - 多轮生成/推荐场景可直接复用权重衰减+正反馈强化的参考特征更新机制，动态调整历史参考/用户偏好的权重，无需额外显式操作即可平衡探索与收敛'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有Agent辅助创意工具的设计空间要么固定、要么持续扩张，完全由用户手动管理收敛过程，无法适配创意工作从早期发散探索到后期收敛细化的阶段需求，导致用户认知负荷高，难以兼顾探索的惊喜性和优化的可控性。
### 方法关键点
- 轴中心动态网格工作流：以用户可配置的2个概念轴控制n×n生成网格，早期探索阶段轴跨度大，覆盖高差异设计方向，输出绑定用户身份特征的可控惊喜结果
- 精细化阶段提供三类核心交互：Zooming（选中单格放大生成局部变异）、Anchoring（锚定多个设计插值生成融合结果）、Decomposition（拆解设计为可拖拽元素/风格/配色token支持重组）
- 后台动态权重机制：参考素材权重随用户正反馈提升，随迭代次数自然衰减，平滑实现从探索到收敛的过渡，无需用户额外显式操作
### 关键结果
14名专业设计师参与的被试内实验，对比无轴交互的基线系统：
- 创意支持指数（CSI）提升24.9%（69.71 vs 55.79，p=0.0085）
- 生成结果多样性（LPIPS）提升21.2%（0.641 vs 0.529，p<0.0001）
- 用户对过程的可控感评分提升37.5%（5.5 vs 4，p=0.019），正向惊喜感评分提升50%（6 vs 4，p=0.028）
### 核心洞察
人机协同创意Agent的核心价值不是单纯提升生成效率，而是通过结构化的可解释交互，让用户从命令发布者转变为协同创作者，兼顾探索的惊喜性和优化的可控性
