---
title: 'Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of
  Intelligence'
title_zh: Mechanist：面向AI智能机制自主发现的多Agent科研系统
authors:
- Mengru Wang
- Junfeng Fang
- Shuofei Qiao
- Zhenqian Xu
- Haoming Xu
- Haoxiong Wang
- Shumin Deng
- Linyi Yang
- Zhixiang Cui
- Xin Xu
affiliations:
- Zhejiang University
- National University of Singapore
- Heriot-Watt University
- Southern University of Science and Technology
- University of California, San Diego
arxiv_id: '2608.12036'
url: https://arxiv.org/abs/2608.12036
pdf_url: https://arxiv.org/pdf/2608.12036
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: Agent 科研自动化 · AI可解释性
tags:
- MultiAgent
- Mechanistic Interpretability
- AI Safety
- Knowledge Graph
- Automated Research
one_liner: 构建整合跨学科知识与可解释性方法库的多Agent系统，自主探索AI模型的内在机制与优化路径
practical_value: '- 多Agent分工+外置结构化内存架构可直接复用：搭建模型评测、效果归因、合规审计类业务Agent时，可参考假设生成/实验/验证/迭代四阶段分工，用外置artifact替代对话共享内存，降低上下文依赖、支持断点续跑

  - 领域KG+预定义方法库的Agent grounding方案可迁移：针对电商推荐/广告模型的可解释性分析、bad case归因场景，可构建业务专用KG+标准化工具库，大幅提升Agent输出方案的专业性与可执行性

  - 机制定位+推理时干预的优化思路可落地：LLM导购、文案生成等场景中，可先定位任务对应的模型注意力头/特征，推理时动态放大对应组件，增益远超prompt tuning，且无需额外训练'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前AI模型能力迭代速度远超人类对其内在机制的理解速度，手动机制探索效率极低，导致模型潜在风险难以及时发现、能力优化缺乏底层理论支撑；现有AI Scientist系统大多聚焦外部科学任务解决，缺乏针对AI模型本身机制的自主探索能力。

### 方法关键点
- 多Agent架构：由中央调度器统筹假设生成、实验执行、结果验证、迭代优化4个专用Agent，各Agent通过外置结构化内存传递信息，支持断点续跑与历史经验复用
- 知识支撑：整合覆盖26个学科的4300万篇论文跨领域KG，以及包含1.3万篇可解释性相关文献的专用KG，支撑跨学科启发的假设生成
- 工具支撑：内置32种机制分析、因果干预、验证的基础方法库，支持Agent自动设计可执行的实验方案

### 关键实验
对比Claude Code、现有AI Scientist系统，在16篇现有论文复现任务中实验执行可靠性更高，生成的假设在新颖性、影响力、可测试性三个维度均优于基线。落地案例包括：1）发现多模态场景下安全风险可通过看似安全的训练数据跨模态传递，学生模型unsafe响应率达48.6%，是基线的2.4倍；2）定位LLM中分离的个人信念与归因信念注意力头，动态放大对应头可使Pythia-410M信念推理精度提升15.3%，远超prompt提示的1.6%增益；3）机制引导DNA序列生成，α-螺旋含量提升12.8个百分点同时保留序列有效性。

### 核心结论
对AI模型的机制理解不是纯学术问题，可直接转化为比prompt tuning更高效的推理优化、风险防控手段。
