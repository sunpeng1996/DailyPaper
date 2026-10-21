---
title: 'Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach'
title_zh: 预训练基座模型Agent能力端到端轻量评估框架ASAP
authors:
- Jiarui Qin
- Junjie Huang
- Yunjia Xi
- Di Yin
- Yong Yu
- Weinan Zhang
- Xing Sun
- Weiwen Liu
affiliations:
- Tencent Youtu Lab
- Shanghai Jiao Tong University
arxiv_id: '2610.19425'
url: https://arxiv.org/abs/2610.19425
pdf_url: https://arxiv.org/pdf/2610.19425
published: '2026-10-13'
collected: '2026-10-21'
category: Agent
direction: Agent能力评估 · 预训练基座模型诊断
tags:
- Agent Evaluation
- Pretrained LLM
- Trajectory Continuation
- Scaffold Adaptation
- Behavioral Analysis
one_liner: 无需SFT或转Chat格式，通过结构化轨迹续接直接评估预训练基座LLM的端到端Agent能力
practical_value: '- 电商/推荐场景定制Agent选型时，可复用ASAP的轻量评估逻辑，无需对所有候选基座做SFT即可快速对比Agent潜力，大幅降低选型成本

  - 可借鉴Markdown+XML混合格式设计交互prompt，相比纯JSON/纯XML更适配基座LLM的续接习惯，提升工具调用、多轮交互的稳定性

  - 垂直领域基座迭代时，可复用ASAP的轨迹行为分解思路，精准定位Agent能力短板（如探索不足、编辑精度低），针对性优化训练数据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent能力评估仅支持后训练的指令跟随模型，预训练阶段依赖静态代理指标，无法观测模型在交互环境的真实执行行为；若对每个预训练checkpoint做SFT再评估，会产生大量额外成本且改变被评估模型本身，无法准确追踪预训练过程中Agent能力的真实演化。

### 方法关键点
- 将Agent交互转化为结构化文本续接任务，保留基座模型原生补全接口，采用Markdown写自由思考、XML标签包裹动作与观测的混合格式，适配预训练数据中的常见文本模式
- 为每个任务前置3步无解决方案泄露的参考轨迹前缀作为少样本引导，所有模型共用同一份前缀保证对比公平
- 仅设置极简恢复机制：首次出现提前空提交、重复动作时给出1次通用提示，不干预具体任务求解，避免轨迹退化

### 关键结果
在SWE-bench Verified、Terminal-Bench 2.1、BrowseComp-Plus三个Agent基准上测试6款开源基座，可清晰区分不同基座能力，SWE-bench上Pass@1跨度从7.12%到37.70%；对比同一次预训练的不同checkpoint，ASAP对Agent能力提升的灵敏度是传统预训练基准（MMLU、GSM8K等）的2~10倍，可分解出接口合规、执行行为、任务结果三层维度的能力变化。

### 核心结论
基座模型已具备可观的Agent能力，后训练主要提升执行稳定性而非从零构建该能力，预训练阶段引入轨迹数据可带来Agent能力的跃迁式提升
