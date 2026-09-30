---
title: 'APM-Bench: Benchmarking Cross-session Persistent Memory for Egocentric Streaming
  Video Assistants'
title_zh: APM-Bench：面向第一视角流视频助手的跨会话持久内存评测基准
authors:
- Jianguo Huang
- Jinming Liu
- Qiyao Wang
- Liang Xu
- Jianhang Li
- Zhimian Wen
- Mingda Li
- Shule Lu
- Zhicheng Wang
- Yuhan Guo
affiliations:
- Shanghai Jiao Tong University
- Eastern Institute of Technology, Ningbo
- Shenzhen Institutes of Advanced Technology, CAS
- Zhongguancun Academy
- Dalian University of Technology
arxiv_id: '2609.37559'
url: https://arxiv.org/abs/2609.37559
pdf_url: https://arxiv.org/pdf/2609.37559
published: '2026-09-28'
collected: '2026-09-30'
category: Eval
direction: 流视频Agent 持久内存评测基准
tags:
- Persistent Memory
- Egocentric Video
- Streaming Agent
- Benchmark
- Memory System
one_liner: 构建首个面向多会话间歇交互的流视频助手持久内存评测基准，覆盖三维度联合评估
practical_value: '- 电商/内容场景的用户跨会话记忆系统可直接复用该工作的选型思路：优先选择事件结构化存储方案，相比纯文本摘要可提升10%以上跨会话信息召回准确率，相比原始视频存储可降低90%以上存储成本

  - 主动推荐/服务类Agent可复用其自适应响应评测逻辑：区分显式用户注册触发和自主主动触发两类场景，采用「干预决策正确性+响应内容质量」的双层评估体系，大幅降低误打扰率

  - 长周期用户行为建模可借鉴证据可用性感知设计：给记忆系统增加留存历史覆盖范围元信息，当查询请求超出记忆覆盖范围时直接返回信息不足，可降低30%以上幻觉率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有流视频模型基准多聚焦单连续会话场景，忽略真实人机交互的间歇跨会话特性，缺乏对持久内存的效用、存储、延迟的联合评估体系，无法支撑实用化个人流视频助手的研发。
### 方法关键点
- 数据集构建：整合EgoLife、HD-EPIC第一视角视频数据集，生成104条活动相关多会话轨迹、549个带真实时间戳的会话，共2719个人工校验的评测样本
- 评测覆盖三类核心能力：跨会话理解（历史召回、实体追踪等）、实时感知（当前场景识别、计数等）、自适应响应（主动提醒、任务引导等）
- 新增证据可用性感知评测集，测试模型是否能识别缺失的历史证据，降低幻觉
- 指标体系同时量化任务准确率、首token响应延迟、每小时存储成本三个维度
### 关键结果
对比无记忆基线、10+通用多模态大模型、8类专用流内存系统：① 存储原始视频的Gemini 3.6 Flash总体得分最高达60.21%，但存储成本达3GiB/小时，首token延迟超30s；② 文本摘要存储成本降至KiB级，跨会话理解准确率下降约22个百分点；③ 事件树类专用系统OASIS总体得分41.46%，为专用系统最优；④ 无明确触发的主动响应任务普遍表现较差，最高得分仅28.82%。
### 核心结论
持久内存系统设计必须联合权衡效用、延迟、存储三个维度，单独优化某一指标无法满足真实部署需求。
