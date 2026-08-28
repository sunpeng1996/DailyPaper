---
title: What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents
title_zh: ACE视角下的LLM Agent智能体数据生成统一分析框架
authors:
- Xingshan Zeng
- Zishan Xu
- Boju Zhang
- Yuzhou Wu
- Lingzhi Wang
- Jianghao Lin
- Liangyou Li
- Yasheng Wang
- Lifeng Shang
- Xin Jiang
affiliations:
- Huawei Technologies Co., Ltd
- Shanghai Jiao Tong University
- Northwestern University (Chicago)
- Harbin Institute of Technology, Shenzhen
- Shenzhen Loop Area Institute
arxiv_id: '2608.27260'
url: https://arxiv.org/abs/2608.27260
pdf_url: https://arxiv.org/pdf/2608.27260
published: '2026-08-26'
collected: '2026-08-28'
category: Agent
direction: Agent 智能体训练数据生成优化
tags:
- Agentic Data
- Data Generation
- ACE Framework
- LLM Agent
- Data Curation
one_liner: 提出ACE三要素准则与因子化数据表示，统一跨域智能体数据生成范式
practical_value: '- 电商导购/搜索Agent训练数据生成可直接复用ACE校验流程：先过Accuracy准入关（验证商品库查询、工具调用、权益规则执行的合法性），再基于当前模型的错误case校准数据Complexity（过滤过简或远超能力边界的样本），最后基于任务类型、交互路径采样保证Diversity，可大幅降低无效数据占比，提升训练效率

  - 可复用因子化(E,q,τ,v)结构拆解业务场景的智能体数据：E对应商品库、工具接口、平台规则，q对应用户咨询/导购任务，τ对应多轮交互轨迹，v对应成交率、用户满意度等验证信号，各模块独立迭代后做一致性校验，降低数据生成的耦合成本

  - 数据校验环节可复用分层检查思路：优先做低成本规则校验（参数格式、接口权限合法性），再做执行校验（模拟调用工具/查库验证返回合理性），最后对高价值样本做模型/人工抽检，在控制标注成本的前提下可提升数据准确率30%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent的交互学习需要环境、任务、动作、反馈四者对齐的高质量数据，但传统指令生成方法仅关注文本合理性，无法保证交互逻辑的一致性；现有智能体数据生成研究按应用领域碎片化组织，缺乏统一的设计与评估框架，导致不同方法难以横向对比，生成数据质量参差不齐，无法适配Agent持续迭代的训练需求。

### 方法关键点
- 提出跨域统一的因子化智能体数据表示`d=(E,q,τ,v)`：E为环境规范（包含工具集、状态、转移规则、接口），q为任务信号，τ为多轮交互轨迹，v为可选验证器，覆盖工具调用、GUI、编码、多智能体、科学发现等所有Agent场景。
- 划分两类生成范式：正向生成按`E→q→τ`顺序，先构建环境再生成适配任务与交互，落地性更强；反向生成以任务/轨迹/结构为锚点，反向补齐其余因子，可精准控制目标训练能力。
- 提出ACE三要素设计准则：Accuracy为最高优先级准入条件，要求四因子逻辑一致可落地；Complexity匹配当前模型能力，将难度控制在可学习区间；divErsity保证环境、任务、交互行为的非冗余覆盖，三者共同构成约束分布优化目标。

### 关键结论
作为领域综述，该研究梳理出智能体数据生成的三大发展趋势：从基于文本 plausibility 的校验转向执行落地的Accuracy校验，从静态难度设定转向模型感知的动态Complexity校准，从表面文本多样性转向行为覆盖的Diversity优化。

### 核心洞察
智能体数据生成的核心挑战不是生成更多数据，而是随着Agent与环境迭代，持续分配有效、有信息量、无冗余的交互经验。
