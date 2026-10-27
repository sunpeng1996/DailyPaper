---
title: 'Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for
  Tool-Use Agents'
title_zh: Trajectory2Gym：面向工具型Agent的决策对齐组合交互合成方法
authors:
- Yihao Hu
- Zhihao Wen
- Yitong Lin
- Siyuan Lu
- Pan Wang
- Wei Wu
- Jiang-Ming Yang
- Tao Lin
affiliations:
- Westlake University
- Ant International
arxiv_id: '2610.33568'
url: https://arxiv.org/abs/2610.33568
pdf_url: https://arxiv.org/pdf/2610.33568
published: '2026-10-23'
collected: '2026-10-27'
category: Agent
direction: Agent工具使用 训练数据构造与训练优化
tags:
- Tool-Use Agent
- Trajectory Curation
- SFT
- Multi-turn Interaction
- LLM Training
one_liner: 通过组合交互合成+决策对齐标注+结构支撑学习大幅提升多尺度LLM的工具使用能力
practical_value: '- 训练电商客服、订单处理类Agent时，不要直接用成功轨迹做SFT，需按决策可见性过滤标注，排除依赖采集方私有信息的动作，避免学到错误路径

  - 多轮交互类Agent训练可采用parent-normalized SFT，按语义交互单元而非单条样本分配权重，避免长对话权重过高，比常规行平均SFT最高提8个百分点

  - 针对稀缺的多步依赖场景（如订单取消→退款→售后流程）、错误恢复场景（如用户信息查询失败后的补全流程），可定向合成交互样本补充训练集，提升复杂场景表现

  - Agent训练数据选型不要只看数据量，需统计组合路径覆盖率、决策对齐率两个核心指标，同等数据量下结构覆盖度比数据规模更重要'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具Agent训练直接筛选成功轨迹做SFT存在两个核心缺陷：一是组合覆盖不足，统计显示40.9%的成功轨迹仅含最多2个监督决策，仅10%包含错误后恢复决策，稀缺的多步依赖、分支场景样本严重不足；二是决策不对齐，成功轨迹中的动作可能依赖采集方私有信息（如未公开的内部ID），Agent可见历史根本无法支撑该动作，训练后易出现幻觉。

### 方法关键点
1. 组合交互合成：针对训练集中覆盖不足的交互路径（如错误恢复、多步状态依赖），定向生成请求和初始状态，在原生环境中执行得到真实交互日志，补足稀缺样本
2. 决策对齐监督：仅将同时满足「执行成功」「动作参数全部来自Agent可见历史」「符合工作流顺序」的动作标注为监督目标，失败调用保留为上下文但不参与损失计算
3. 结构支撑学习：按模型规模给每条交互路径设定目标样本量，优先补足覆盖不足的路径；训练时采用parent-normalized SFT，按语义交互单元分配权重，避免长对话损失占比过高

### 关键结果
在1.7B~30B共5个尺度的Qwen3模型上验证，对比原生初始化，Tau1、Tau2、BFCL三个基准的平均得分提升16.9~29.8个百分点；4B模型训练后的Tau2得分（69.17）超过原生30B-A3B模型（28.33）；消融实验显示parent-normalized SFT单独贡献8.04个点的提升。

### 核心结论
成功只能证明轨迹的最终结果正确，不能证明每个动作都可被Agent从可见历史中学到，轨迹的价值取决于它实现的依赖关系和可见历史能支撑的决策，而非最终成败。
