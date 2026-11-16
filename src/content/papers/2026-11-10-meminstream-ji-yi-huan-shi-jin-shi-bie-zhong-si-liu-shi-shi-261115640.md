---
title: 'MemInStream: Memorizing or Merely Recognizing? Rethinking Streaming Video
  Memory Evaluation'
title_zh: 《MemInStream：记忆还是仅识别？重思流式视频记忆能力评估》
authors:
- Zhenqi He
- Dunyuan Xu
- Yang Bo
- Kien T. Pham
- Yanghao Wang
- Shuhan Li
- Xintong Guo
- Yuyang He
- Fang Liu
- Huankang Guan
affiliations:
- HKUST
- CUHK
- Huawei Research
- CityU
arxiv_id: '2611.15640'
url: https://arxiv.org/abs/2611.15640
pdf_url: https://arxiv.org/pdf/2611.15640
published: '2026-11-10'
collected: '2026-11-16'
category: Eval
direction: 流式视频理解 · 记忆能力评测
tags:
- Streaming-Video
- Memory-Evaluation
- Benchmark
- Video-Understanding
- QA
one_liner: 提出带证据控制验证协议的流式视频理解记忆能力专属评测基准MemInStream
practical_value: '- 做长时交互Agent（直播导购Agent、长会话推荐Agent）的记忆能力评测时，可复用证据控制验证协议，排除不用历史记忆就能答对的捷径问题，避免评测虚高

  - 设计长序列推荐/搜索的记忆模块评测指标时，可参考MemInStream的四类任务划分：Episodic Retrieval、State Tracking、Multi-Evidence
  Integration、Contextual Memory，覆盖不同记忆场景

  - 做直播/短视频内容理解的流式处理模型迭代时，可直接用MemInStream基准验证长时记忆模块的真实效果，避免把理解错误误判为记忆失效'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有流式视频理解的记忆相关评测仅依赖QA准确率，无法区分预测错误来自视觉理解失效还是记忆遗忘，正确预测也可能来自语言先验、近期观测而非历史记忆，无法准确衡量模型真实记忆能力。

### 方法关键点
1. 提出MemInStream专属记忆能力评测基准，设计证据控制验证协议，为每个问题绑定时间局部化的证据区间；
2. 通过过滤规则仅保留「仅靠标注证据可回答、仅靠近期观测/证据后观测/纯文本输入无法回答」的问题，实现记忆限制与理解失效的解耦，消除不依赖记忆的答题捷径；
3. 覆盖四类核心记忆评测任务：Episodic Retrieval、State Tracking & Updating、Multi-Evidence Integration、Contextual Memory，适配多类视频场景。

### 关键结果
基准及配套数据集已开源，可系统性衡量流式视频模型的真实记忆能力，当前主流模型在该基准上的表现远低于人类表现。
