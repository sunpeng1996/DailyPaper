---
title: 'Omni-InteractScope: Benchmarking Proactive and Agentic Interaction in Continuous
  Omnimodal Streams'
title_zh: Omni-InteractScope：连续全模态流主动智能交互基准
authors:
- Yinsong Yan
- Ling Wang
- Yuxuan Wang
- Yifan Yang
- Ruiyang Xu
- Junming Lin
- Qi Chen
- Meng Gao
- Minghao Han
- Yunfei Chu
affiliations:
- The Hong Kong Polytechnic University
- Alibaba Token Hub, Alibaba Group
- Shanghai Jiao Tong University
- Tsinghua University
- Fudan University
arxiv_id: '2610.35439'
url: https://arxiv.org/abs/2610.35439
pdf_url: https://arxiv.org/pdf/2610.35439
published: '2026-10-25'
collected: '2026-10-28'
category: Agent
direction: 多模态Agent · 流交互能力评测
tags:
- Agent
- Omni-LLM
- Benchmark
- Proactive Interaction
- Streaming Perception
one_liner: 发布含1479条标注样本的全模态流主动交互基准，揭示当前Omni-LLM三大能力缺陷
practical_value: '- 做主动交互Agent（如直播电商导购、实时场景提醒类产品）时，不能仅看工具调用准确率，必须加「无场景输入对照测试」，避免模型靠请求先验蒙对结果

  - 做无query主动提醒场景（如直播关键信息推送、用户行为预警）时，可引入响应历史降低58%输出量且不损失召回；10s响应冷却会降低9.84pp召回，需权衡体验和准确率

  - 多步引导类Agent（如客服引导、下单流程辅助）的评估需新增完整序列覆盖率指标，单步准确率高不代表全流程可达标'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Omni-LLM在连续音视频流场景下的主动交互能力缺乏系统性评测，现有基准无法衡量模型结合流证据、用户需求输出及时、持续干预的可靠性，无法支撑主动交互类Agent的落地迭代。

### 方法关键点
- 基准覆盖8类任务：事件定时工具调用、通知、风险预警、状态追踪、非语言/工作流 cue 响应、连续回复、无障碍辅助，含1479条人工标注交叉校验的交互样本，对应1790个带时间窗的响应目标
- 评测维度同时校验响应内容正确性、触发时机准确性、多步序列覆盖率，区分显式请求响应、无query主动提醒两类场景
- 设计多组对照实验：分别测试有无场景输入、不同响应策略（有无历史、冷却时间）、有无显式事件 cue 对结果的影响

### 关键结果
评测12款主流Omni-LLM（含闭源Gemini、Qwen系列，开源InternVL3.5、Qwen系列，流式模型LiveCC、MiniCPM-o等），核心数据：
1. 定时工具调用联合准确率最高仅32.0%，准时响应率最高不足40%
2. 无query主动提醒的准时召回率最高仅23.0%，远低于同场景显式QA的62.3%
3. 多步引导单步召回最高51.7%，但全序列完成率最高仅3/26，9款模型全序列覆盖率为0

### 最值得记住的一句话
主动交互Agent的评估不能只看单步内容准确率，必须同时校验触发时机、场景依赖、全序列覆盖三个维度，否则结果会严重高估实际落地能力
