---
title: 'VideoJSON: A Minimal Harness Beats Purpose-Built Memory for Ultra-Long Video
  Understanding'
title_zh: VideoJSON：极简架构超越专用内存实现超长视频理解
authors:
- Wenqi Marshall Guo
- Kuan-Hao Huang
- Junda Chen
- Hao Zhang
affiliations:
- University of British Columbia
- National Taichung University of Education
- University of California, San Diego
arxiv_id: '2611.28167'
url: https://arxiv.org/abs/2611.28167
pdf_url: https://arxiv.org/pdf/2611.28167
published: '2026-11-19'
collected: '2026-11-25'
category: Agent
direction: Agent 长时序多模态理解架构设计
tags:
- Coding Agent
- Structured Memory
- Ultra-long Video Understanding
- RAG
- Model Distillation
one_liner: 基于每分钟结构化JSON+编码Agent自写搜索的超长视频理解SOTA架构
practical_value: '- 电商用户长周期行为理解可复用该架构：将用户每段行为（点击/浏览/下单）转化为固定schema的结构化JSON记录，让编码Agent自主编写Python/Bash脚本做多步检索统计，替代固定召回/SQL逻辑，灵活适配复杂自定义查询需求（如「用户过去3个月每次大促后3天的品类偏好」）

  - 结构化记忆落地trick：无需提前构建复杂知识图谱、多粒度索引，仅为每个时序片段预设高信息密度的结构化字段，性能优于专用复杂内存架构，工程落地成本降低60%以上

  - 小模型低成本蒸馏方案：采集大模型生成的多步搜索轨迹做LoRA SFT，仅64条无关场景的轨迹就能让小模型（Qwen-3.5-Flash）任务性能提升最高8.25点，可快速落地边缘端Agent、低算力业务场景

  - 多轮Agent成本优化：利用KV cache复用会话前缀，89.7%的输入token可缓存，大幅降低多步推理的调用成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有超长视频理解系统依赖复杂专用内存图、固定检索pipeline，灵活性差，无法适配任意多步查询需求，且模型能力提升无法直接转化为系统性能增益，工程落地成本高。

### 方法关键点
- 索引阶段：用VLM将每分钟视频转为单条JSON记录，包含dense caption、事件、实体、地点、语音转录等固定schema结构化字段，一次性批量构建全量索引，无需多粒度聚合、知识图谱构建
- 查询阶段：给编码Agent开放沙箱Python/Bash执行权限，Agent可自主编写多步搜索脚本对JSON记录做过滤、关联、统计，无需任务微调也无需访问原始视频
- 扩展能力：支持叠加视频QA、外部决策API等工具，也可将大模型生成的搜索轨迹做SFT蒸馏到小模型，降低部署成本

### 关键实验
在4个超长视频基准（EgoLifeQA、Ego-R1-Bench、MM-Lifelong、EgoMemReason）测试：用DeepSeek V4.1 Flash的VideoJSON分别超越MAGIC-Video 7.0、20.0、24.75分，超越最优之前方案EgoMemReason 12.6分；模型能力越强增益越大，最强模型相对最弱模型增益11.58分，是MAGIC-Video的2倍以上；仅用64条无关场景的搜索轨迹SFT Qwen-3.5-Flash，MM-Lifelong得分最高提升8.25分。

### 核心记忆点
做长时序Agent系统时，优先把资源投入到结构化单条记录的信息密度上，把检索逻辑完全交给Agent自主实现，系统性能会随模型能力提升自然增长。
