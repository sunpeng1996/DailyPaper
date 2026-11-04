---
title: You don't need long context
title_zh: 无需长上下文：通过高频压缩实现LLM短上下文高效推理
authors:
- Peter Belcak
- Saurav Muralidharan
- Jindong Jiang
- Yonggan Fu
- Wonmin Byeon
- Hanrong Ye
- Ryan Angilly
- Ali Taghibakhshi
- Shih-Yang Liu
- Siru Ouyang
affiliations:
- NVIDIA
arxiv_id: '2611.05306'
url: https://arxiv.org/abs/2611.05306
pdf_url: https://arxiv.org/pdf/2611.05306
published: '2026-11-02'
collected: '2026-11-04'
category: LLM
direction: LLM推理效率优化 · 上下文压缩
tags:
- Context Compression
- LLM Inference Optimization
- Agent Workflow
- Cost Efficiency
- Semantic State Space Model
one_liner: 验证短上下文配合压缩与选择性读取可媲美长上下文效果，推理成本最高降7倍
practical_value: '- 电商/导购Agent可替换全量对话历史累加机制，采用EoCC阈值压缩将上下文控制在16-32K，推理成本最高降7倍，90%以上场景精度损失小于2pp

  - 长文本类业务（如商品评论分析、合规审核）无需全量加载长文档，用选择性读取工具将长输入转为多步短上下文任务，部分场景精度可提升最高40pp，成本降数十倍

  - 高并发Agent场景（如大促智能客服）可采用SAC单步压缩机制，仅维护语义状态，峰值上下文压缩到7-9K，硬件吞吐量提升3.6-7倍，适配边缘/端侧部署'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM上下文窗口持续扩张，但长上下文下token生成成本、latency随上下文长度线性增长：256K上下文下生成1M tokens的成本是16K的3.6~7倍，收益等同于甚至超过量化、稀疏化等优化手段，而长上下文是否为长任务的必要条件尚未被系统性验证。

### 方法关键点
- 设计三类上下文管理机制：FHA全历史累加（基线）、EoCC阈值触发压缩（上下文达到预设阈值时，让LLM输出任务相关紧凑状态，重启新会话继续执行）、SAC单步压缩（每执行1次动作就压缩1次上下文，仅保留核心语义状态）
- 长输入任务改造：将长文档存入文件系统，给Agent开放sed/awk等读取工具，把长输入任务转化为长horizon多步任务，避免全量加载到上下文
- 覆盖13个长场景benchmark，包括SWE-bench代码任务、LongBench v2长文档QA、NIAH大海捞针等，测试Claude Opus 4.5、GPT 5.6 Sol两款前沿闭源模型

### 关键结果
- 长horizon任务：EoCC将上下文压缩到16~48K时，精度波动在±3.7pp以内，90%以上场景精度损失小于2pp，推理成本降2.2~8.8倍
- 长输入任务：配合选择性读取，精度最高比全量输入基线提升40pp，成本降4.4~233.3倍，会话总长度不随文档长度线性增长
- SAC单步压缩：峰值上下文仅7~9K，比基线最多降90%，精度损失最高3.3pp，无灾难性下降

长上下文不是完成长任务的必要条件，合理的状态维护和选择性读取可在短上下文下实现同等甚至更好的效果，同时大幅降低推理成本。
