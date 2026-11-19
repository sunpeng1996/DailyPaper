---
title: 'VideoACE: Benchmarking Agentic Video Understanding through High-Frame-Rate
  Actions'
title_zh: VideoACE：面向高帧率动作场景的智能体视频理解评测基准
authors:
- Luoyuan Zhang
- Xuanyu Zheng
- Yancheng Long
- Haoyang Xu
- Bin Wen
- Tingting Gao
affiliations:
- KlingAI Research
arxiv_id: '2611.24184'
url: https://arxiv.org/abs/2611.24184
pdf_url: https://arxiv.org/pdf/2611.24184
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: 智能体视频理解能力评测基准
tags:
- Agent
- Video Understanding
- Benchmark
- Interactive Evaluation
- Multimodal Reasoning
one_liner: 推出支持交互评估的高帧率动作视频理解基准VideoACE，含1000道多类别带标注评测题
practical_value: '- 短视频电商内容理解Agent可复用其「可调采样帧率+时空粒度按需调取」的工具调用设计，提升快动作类内容（如美妆手法、运动器材演示）的理解准确率

  - 视频类推荐系统的内容打标场景可参考其细粒度时序证据标注规范，降低高帧率动作内容的标签错误率，提升推荐冷启动精度

  - 多模态Agent的交互能力评测可复用其「单遍观测→自主工具调用→用户反馈修正」的三阶评测范式，对齐真实业务的用户交互流程'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频理解评测多采用固定观测设置，无法衡量智能体主动交互、按需调取视频信息的能力，尤其缺乏高帧率场景下快速细微动作理解的针对性评测方案。

### 方法关键点
1. 构建VideoACE评测基准，覆盖6类细粒度动作理解场景，包含1000道经过答案泄露筛查的多选题，配套时序证据标注与合规用户提示；
2. 评测环境整合视频检查工具与用户模拟器，支持模型自主调整时间覆盖范围、采样密度、空间细节，可基于模拟用户反馈回溯证据、修正判断；
3. 设置三类评测范式：单遍观测、自主工具调用、工具调用+用户反馈，全面衡量模型对交互机会的利用效率。

### 关键结果
对5款主流模型的评测显示，不同模型在证据获取路径、交互响应模式上存在显著差异，该基准可有效区分固定观测性能之外的智能体视频理解实际能力。
