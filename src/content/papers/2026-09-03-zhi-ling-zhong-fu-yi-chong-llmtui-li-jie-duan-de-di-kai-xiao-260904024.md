---
title: Instruction Duplication as an Inference-Time Control Primitive
title_zh: 指令重复：一种LLM推理阶段的低开销控制原语
authors:
- Victor Lavrenko
affiliations:
- PeaceTech VC, Israel
arxiv_id: '2609.04024'
url: https://arxiv.org/abs/2609.04024
pdf_url: https://arxiv.org/pdf/2609.04024
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: LLM推理控制 · 零成本指令优化
tags:
- Inference Control
- Prompt Engineering
- Instruction Following
- Trajectory Editing
- Black-box Optimization
one_liner: 无需训练/修改解码，仅重复流程指令即可提升LLM输出轨迹的机器可解析合规性，不影响最终答案准确率
practical_value: '- 做Agent工具调用/推荐理由生成场景时，可在prompt末尾重复一次流程指令（比如“请严格按照【事实-备选-决策】结构输出”），无需额外训练就能降低30%左右的下游格式解析失败率，不会影响输出内容质量。

  - 做LLM驱动的推荐文案/搜索query改写的自动化质检时，可优先采用指令重复方案，输出准确率不受影响的同时，减少人工校验的成本。

  - 部署带轨迹编辑能力的LLM应用（比如电商智能客服、动态推荐理由生成）时，可测试指令重复+后置的组合，医疗场景实测该方案能将下游编辑器的处理成功率从84.2%提升到97.1%。

  - 注意规避副作用：指令重复会小幅提升模型过早输出最终结果的概率，需在业务侧增加对应校验规则拦截异常输出。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM系统的输出不仅要求最终答案正确，还要暴露可被下游控制器/编辑器解析的中间状态，但现有推理阶段控制方案要么需要微调模型、要么需要修改解码逻辑，落地成本高；而全prompt重复会引入大量冗余内容，仅针对流程指令的轻量化控制方案存在空白。

### 方法关键点
- 定义指令重复机制：仅重复流程类指令I，不重复业务Query Q，支持在system位、query前、query后三个位置自由组合，完全黑盒，无需训练、无需修改解码逻辑。
- 采用2×2×2因子实验设计，覆盖0~3份指令副本、8种放置组合，在7款主流指令调优LLM上开展测试。
- 评估指标做三类拆分：流程合规性（All-8诊断、预承诺TF-IDF召回、角色完成度）、最终答案准确率、副作用（过早承诺率）。

### 关键实验
数据集为300道医学多选题，共完成16646次有效生成，对比基线为单份指令的常规prompt：
- 从1份指令升级到2份，All-8流程合规率从90.22%升至93.17%，减少30.2%的解析失败；预承诺TF-IDF召回从73.44%升至74.81%，Holm校正后p<0.001；最终答案准确率完全保持60.21%不变；仅过早承诺率从1.52%小幅升至2.30%。
- 下游Answer Engineering（AE）轨迹编辑任务中，添加尾部重复指令将SSNHL分支处理成功率从84.2%提升至97.1%。

### 最值得记住的一句话
如果LLM输出是给下游程序消费的API，那么提升显式中间状态的可观测性，比单纯提升答案准确率对系统的业务价值更大。
