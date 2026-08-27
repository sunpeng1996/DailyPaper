---
title: 'Automata from Agent Traces: Failure and Next-Step Prediction'
title_zh: 基于LLM Agent执行轨迹构建自动机实现失败与下一步预测
authors:
- Seonglae Cho
- Franklin Cardenoso Fernandez
- Umar Mohammed
- Zekun Wu
- Kleyton Da Costa
- Ilham Wicaksono
- Adriano Koshiyama
affiliations:
- Holistic AI
- PUC-Rio
- University College London
arxiv_id: '2608.23670'
url: https://arxiv.org/abs/2608.23670
pdf_url: https://arxiv.org/pdf/2608.23670
published: '2026-08-23'
collected: '2026-08-27'
category: Agent
direction: Agent行为建模与运行时监控
tags:
- LLM Agent
- Finite State Machine
- Runtime Monitoring
- Failure Prediction
- Workflow Memory
one_liner: 无超参数从Agent轨迹构建紧凑FSM，统一支撑工作流记忆、预测与运行时监控
practical_value: '- 电商客服Agent、多Agent推荐系统的运行时监控可直接复用该FSM构建方案，无超参数、毫秒级构建，32%执行进度即可触发失败提前终止，节省68%冗余算力

  - 做Agent工作流记忆时不要输出全量结构上下文，仅返回当前状态的下一跳概率+Top15多步延续的极简格式，比AWM方案平均提升12%以上的下一跳预测准确率

  - Agent失败预测可直接复用FSM的交叉熵异常特征、单状态访问频率等特征，无需复杂模型即可达到最高0.94的AUROC，还能为MLP/GRU等序列模型带来稳定效果提升

  - 若你的Agent动作空间有限（比如工具调用、固定流程交互），这套FSM方案可直接替代定制化的行为建模、异常检测管线，一套结构覆盖多类需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent执行多步任务时轨迹结构不透明，现有方案要么单轨迹处理要么仅用成功轨迹，无法支撑落地需要的安全审计、运行时监控，也没法挖掘跨运行的拓扑结构关联下一跳和失败预测。

### 方法关键点
1. 先从轨迹中抽取活动符号，优先级为工具调用名>动作标签>命令语义分类，无匹配时默认角色+内容类型；
2. 构建前缀树后按最后一步活动合并状态，仅过滤掉仅出现1次且不是源状态唯一出口的转移，全程无超参数；
3. 基于FSM状态统计转移概率，提取交叉熵、访问频率等特征用于预测和监控。

### 关键实验
基于12个公开数据集，对比RPNI、Alergia、AWM等9类基线：生成的FSM仅7-43个状态，测试回放fitness≥0.997，构建耗时毫秒级；下一跳预测在8个数据集上全部优于AWM，最高提升25.3pp；失败预测最高AUROC达0.94，仅需50%执行进度即可达到92%的全轨迹AUROC，运行时监控可在32%进度时触发提前终止，精度85.9%、召回95.5%。

### 核心结论
LLM Agent的行为拓扑更多由部署框架而非大模型本身决定，有限动作空间下的紧凑FSM是可落地的多用途结构原语。
