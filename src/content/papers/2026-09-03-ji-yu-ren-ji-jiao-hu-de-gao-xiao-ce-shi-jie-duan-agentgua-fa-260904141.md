---
title: Efficient Test-Time Adaptation through Human-AI Interaction
title_zh: 基于人机交互的高效测试阶段Agent适配方法
authors:
- Zora Zhiruo Wang
- Apurva Gandhi
- Rulin Shao
- Aspen Chen
- Jonas Mueller
- Zhiqi Liang
- Jett Chen
- Michael Ryan
- Qianou Ma
- Luxi He
affiliations:
- Carnegie Mellon University
- University of Washington
- Handshake AI
- Stanford University
- Princeton University
arxiv_id: '2609.04141'
url: https://arxiv.org/abs/2609.04141
pdf_url: https://arxiv.org/pdf/2609.04141
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: Agent 测试时个性化适配与人机交互
tags:
- Test-Time Adaptation
- Human-AI Interaction
- LLM Agent
- LoRA
- DPO
one_liner: 提出结合人交互信号的上下文+权重双路测试时适配方案与动态评分规则模块，大幅提升Agent个性化任务成功率
practical_value: '- 电商/广告场景的个性化Agent（比如商家专属文案生成、智能美工、客户服务Agent）可复用双路适配逻辑：短期用上下文记忆沉淀用户（如商家、运营）的显性偏好，长期用DPO+LoRA微调固化隐性风格要求，既保证可解释性又避免上下文窗口过载

  - 可直接复用动态rubric模块设计，在运营人员审核Agent输出（营销文案、商品海报、商品标题）的交互过程中自动提炼评价规则，比人工/纯LLM生成的评估标准多捕捉16%-22%的不合格case，大幅降低个性化评估的人工成本

  - 收集用户反馈不要局限于文本评价，可新增输出内容直接编辑、执行计划调整、评分结果修正等多通道信号，相比仅用文本反馈能额外带来3%-7.6%的性能提升，同时降低用户反馈门槛'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
泛化训练的LLM Agent输出同质化严重，无法满足专业用户的个性化、隐性任务要求，尤其在文案创作、视觉生成这类开放任务中，用户偏好很难提前明确表述；现有Agent适配方案大多仅利用单次交互的文本反馈，跨会话的多模态交互信号未被充分挖掘，亟需能在几十次任务内快速对齐用户偏好的高效测试时适配方案。
### 方法关键点
- 设计多通道人机交互接口，支持用户提供4类反馈信号：文本留言、执行计划调整、输出内容直接编辑、评价规则修改，覆盖各类隐性偏好的表达场景
- 双路适配机制：①上下文适配：将交互信号自动提炼为事实偏好记忆和流程技能库，注入Agent上下文；②权重适配：基于交互前后的Agent输出构造DPO偏好对，用LoRA轻量微调更新模型权重，避免上下文窗口持续膨胀
- 动态rubric模块：自动从交互信号中提炼可落地的二进制评价规则，支持人工修正，作为Agent适配的统一评估依据
### 关键结果
在学术摘要写作、数据可视化两个开放任务上，对30名用户共600个任务做适配：
- 仅需20次任务交互，上下文适配可提升任务成功率4.5%-12.9%，权重适配可提升4.5%-20.9%，跨任务泛化成功率提升2.4%-5.8%
- 动态生成的rubric比纯LLM、纯人工生成的评价规则多捕捉16.0%-22.3%的不合格输出
- 权重适配比上下文适配减少62.6%-88.3%的输入token，推理效率更高
### 核心结论
AI Agent未来不应该是千篇一律的通用工具，而是通过持续交互动态适配用户个性化需求的专属助手，少量交互数据即可达成可观的个性化效果
