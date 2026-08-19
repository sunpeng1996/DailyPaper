---
title: 'aDSL: Agentic 3D Creation via Joint Agent-Program Design'
title_zh: aDSL：面向智能体3D创作的DSL与多智能体系统联合设计
authors:
- Rui-Huan Wang
- Si-Tong Wei
- Jia-Qi He
- Heng-Yi Wei
- Baoquan Chen
- Peng-Shuai Wang
affiliations:
- Peking University
arxiv_id: '2608.17975'
url: https://arxiv.org/abs/2608.17975
pdf_url: https://arxiv.org/pdf/2608.17975
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: 多智能体协作 · DSL与工作流联合设计
tags:
- Multi-Agent
- DSL
- 3D Generation
- Plan-Execute-Critic
- Training-Free
one_liner: 联合设计面向智能体的3D专属DSL与免训练多智能体系统，提升3D生成鲁棒性与可控性
practical_value: '- Agent工作流可直接复用：采用Planner/Coder/Critic/Debugger的角色分工+Plan-Execute-Critic自闭环，搭配选择性内存机制避免上下文溢出，适合电商智能文案生成、商品信息结构化等长序列任务

  - 领域DSL设计思路可迁移：针对LLM擅长语义/关系推理、弱于精准数值计算的能力边界定制DSL，用声明式关系算子代替硬编码数值，降低生成错误率，可用于电商商品属性抽取、定制化内容生成等场景

  - 免训练落地路径可参考：无需LLM微调，仅通过DSL与工作流的协同设计即可提升任务效果，大幅降低中小业务团队的Agent系统落地成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于LLM的程序化3D生成方案鲁棒性差，常出现组件漂浮、对齐错误等问题，核心原因是现有编程接口与LLM能力不匹配：LLM擅长语义结构拆解、空间关系推理，但对精准数值坐标、底层API调用的容错率极低，微小误差就会导致生成结果不符合需求。

### 方法关键点
- 联合设计Agent-centric DSL（aDSL）：同时满足三个特性，①表达性：内置几何基元、布尔运算、变换算子，支持复杂形状构建；②可组合性：基于Python类实现层级化组件定义，支持复用与局部修改；③空间推理：内置对齐、分布等声明式布局算子，无需手动计算绝对坐标即可实现约束满足。
- 免训练多智能体系统：采用Plan-Execute-Critic闭环，Planner负责拆解需求为组件结构、空间约束、校验清单；Coder生成aDSL代码，Executor执行后输出3D结构与多视角渲染图；Debugger修复执行报错；Critic结合渲染结果与代码校验约束，输出可落地的修复反馈。
- 选择性内存机制：持久化存储用户原始需求与Planner输出，滑动窗口仅保留最新代码与反馈，避免上下文溢出同时保证目标不偏移。

### 关键结果
- 文本转3D任务：在100个来自ShapeNet/ABO/Objaverse的样本、200条prompt上，相比同类型代码生成基线，CLIP得分最高提升1.93，VQA得分最高提升6.21，执行成功率稳定100%；用户评估中85.39%的参与者认为其prompt对齐更优，86.84%认为几何质量更好。
- 图片转3D任务：在Toys4K数据集上，代码生成类方法中CLIP得分最高达84.42，FID最低。

最值得记住的结论：面向LLM的领域系统优化，无需一味提升模型能力，通过DSL与Agent工作流的联合设计匹配LLM的能力边界，能以极低的训练成本大幅提升任务效果与鲁棒性。
