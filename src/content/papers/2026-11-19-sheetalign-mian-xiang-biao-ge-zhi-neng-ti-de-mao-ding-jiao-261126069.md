---
title: 'SheetAlign: Grounded Interaction and Stage-Isolated Learning for Spreadsheet
  Agents'
title_zh: SheetAlign：面向表格智能体的锚定交互与阶段隔离学习框架
authors:
- Yuxiang Wang
- Junhao Gan
- Jianzhong Qi
affiliations:
- The University of Melbourne
arxiv_id: '2611.26069'
url: https://arxiv.org/abs/2611.26069
pdf_url: https://arxiv.org/pdf/2611.26069
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: 表格Agent 小参数LLM优化
tags:
- Spreadsheet Agent
- Grounded Interaction
- GRPO
- LoRA
- Execution Consistency
one_liner: 结合锚定交互、阶段隔离强化学习与执行一致性的轻量表格智能体框架
practical_value: '- 垂直场景小参数Agent落地可先引入任务锚定流程：生成操作前先让LLM输出结构化任务拆解（操作位置、依赖数据、所需API），仅传入任务相关上下文，零训练即可大幅提升准确率，论文中该操作让Qwen3-4B准确率提升15.7个百分点

  - 多步任务RL训练可采用阶段隔离+细粒度进度奖励：拆分生成、校验两个独立策略，用编辑F1替代全对全错的0/1奖励，能充分利用部分正确样本，降低训练难度，稳定提升效果

  - 推理阶段多候选选择优先采用执行结果一致性：无需训练额外排序模型，直接比对多个候选执行后的输出状态（如表格修改结果、推荐候选集合），成本低收益稳定，效果优于训练得到的选择器

  - 执行错误可引入定向诊断修复：针对代码执行报错、输出异常给出明确诊断信息，让LLM仅修正错误部分无需全局重写，能提升近7个点的执行成功率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
企业日常运营、数据分析大量依赖表格操作，现有闭源表格智能体存在数据泄露风险、调用成本高的问题，而开源小参数LLM落地表格场景存在三大痛点：生成的操作容易命中错误单元格，缺乏任务到执行的锚定；全任务0/1奖励无法区分部分正确的执行结果，训练信号稀疏；LLM生成稳定性差，单次输出可靠性低。
### 方法关键点
- 锚定任务交互：生成操作代码前，先让LLM输出结构化任务描述（操作位置、数据源、操作类型、所需API），仅向模型返回任务相关的表格上下文和API参考，缩小生成范围
- 阶段隔离学习：基于GRPO+LoRA分别训练生成策略、校验策略两个独立分支，用细粒度的编辑进度F1奖励替代全对全错奖励，鼓励模型完成部分正确的操作
- 执行一致性选择：推理阶段采样4个候选（2个来自基础策略、2个来自生成策略），比对执行后的表格状态指纹，选择占比最高的结果，再经校验策略修正
### 关键实验
在SpreadsheetBench（912个真实表格任务）、Domain-Spreadsheet（1660个跨领域表格任务）上验证，基线为同参数的Spreadsheet-RL、SheetAgent等。核心结果：零训练的锚定交互将Qwen3-4B平均准确率从13.5%提升到29.2%；加阶段隔离学习、执行一致性后，SpreadsheetBench平均准确率达32.8%，Domain-Spreadsheet达30.1%，比同参数基线高9.4个百分点，执行成功率达98.6%。
> 最值得记住的结论：小参数垂直Agent的优化优先做任务锚定、执行层的零训练优化，收益远大于纯强化学习训练的收益
