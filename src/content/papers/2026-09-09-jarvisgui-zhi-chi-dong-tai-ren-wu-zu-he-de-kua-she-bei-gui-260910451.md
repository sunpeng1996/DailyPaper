---
title: 'JarvisGUI: Towards Cross-Device GUI Agents with Dynamic Task Composition'
title_zh: JarvisGUI：支持动态任务组合的跨设备GUI Agent评测基准
authors:
- Zixiang Chen
- Yuheng Lu
- Zihao Cheng
- Zeming Liu
- Jizeng Bai
- Ziye Huang
- Zhiyin Lin
- Zihan Li
- Yuhang Guo
- Yunhong Wang
affiliations:
- Beihang University
- Beijing Institute of Technology
- Baidu Inc.
arxiv_id: '2609.10451'
url: https://arxiv.org/abs/2609.10451
pdf_url: https://arxiv.org/pdf/2609.10451
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: GUI Agent 跨设备协作能力评测
tags:
- GUI Agent
- Cross-Device Agent
- Benchmark
- Multimodal LLM
- Task Composition
one_liner: 首个覆盖多操作系统的跨设备GUI Agent评测基准，揭示现有模型跨平台协作短板
practical_value: '- 跨多端（APP/PC/H5）的用户操作Agent可复用Planner-Grounder架构，上层做跨端路径规划、下层做单端动作落地，无需全量重训现有单端GUI
  Agent

  - 复杂多步任务自动生成可借鉴基于类型系统的任务组合方法，通过输入输出slot类型匹配自动拼接子任务，大幅降低人工标注成本，适合生成电商多端联动的模拟用户行为数据集

  - 多端Agent评测可参考其基于最终环境状态的自动校验逻辑，通过程序检查文件、界面元素状态完成评估，避免人工评测的高成本，适合业务端回归测试'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有GUI Agent评测基准均基于单设备假设，完全忽略真实场景中用户跨手机、PC、服务器协作完成任务的普遍需求，导致对Agent实际落地能力的评估过于乐观，缺乏系统性的跨设备能力评测框架。

### 方法关键点
- 设计层级类型系统定义任务的输入输出slot，通过子类型兼容规则自动校验任务拼接的合法性，支持大规模动态生成跨设备多步任务
- 搭建4层架构的标准化评测环境，基于Docker+KVM实现Android/Windows/Ubuntu多系统隔离部署，通过统一抽象接口屏蔽底层平台差异，支持高吞吐并行评测
- 采用Planner-Grounder双层架构适配现有单设备GUI Agent：上层通用VLM接收多端截图做跨平台任务规划，下层专用Grounding Agent执行单端精确动作定位

### 关键实验
基准包含118个单平台原子任务、150个组合任务（含50个跨设备带依赖任务），评测7款SOTA开源GUI Agent。结果显示：原子任务平均总成功率（TSR）最高仅42.4%，跨设备带依赖任务的TSR最高仅8.0%，4步以上多步任务成功率接近0，单设备能力与跨设备能力存在显著断层。

### 核心结论
跨设备任务中的状态传递感知、跨平台上下文推理、长依赖链路管理是当前GUI Agent落地的核心瓶颈，远未达到可用水平。
