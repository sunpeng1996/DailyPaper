---
title: 'OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video'
title_zh: OneSearch-VL：面向图像与视频的统一多模态深度研究Agent
authors:
- Hongyu Li
- Manyuan Zhang
- Kaituo Feng
- Shu Chen
- Dian Zheng
- Hao Li
- Hao Yu
- Zhangquan Chen
- Zoey Guo
- Ray Zhang
affiliations:
- BUAA
- CUHK
- NTU
- THU
- HFUT
arxiv_id: '2610.12419'
url: https://arxiv.org/abs/2610.12419
pdf_url: https://arxiv.org/pdf/2610.12419
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: 多模态Agent · 跨视觉模态统一研究
tags:
- Multimodal Agent
- Visual Grounding
- Evidence Graph
- Reinforcement Learning
- VQA
one_liner: 提出VGEG统一结构，实现单图、多图、视频跨模态深度研究的多模态Agent框架
practical_value: '- 可复用VGEG结构搭建电商多模态素材知识图谱：将商品主图/详情图/视频中的视觉锚点（logo、版型、成分标）、商品属性、外部知识（用户评价、同类品信息）关联，支撑商品问答、个性化推荐理由生成、虚假宣传检测等业务

  - 参考EVGR奖励优化推荐Agent的RL训练：在传统点击/转化目标之外，新增「推荐理由与商品属性匹配度」（证据可追溯）、「推荐依据与用户提交的图文/视频素材匹配度」（视觉锚定）两个奖励维度，减少推荐幻觉，提升可解释性

  - 跨视觉类型统一训练方案可直接复用：电商场景同时存在单图、组图、视频三类商品素材，训练多模态理解模型时混合三类数据，相比单类型训练平均提升4%左右的效果，且不会牺牲单任务性能

  - VGEG数据引擎可降低多模态Agent训练数据标注成本：参考「视觉锚点发现→外部知识关联→任务自动生成→专家轨迹过滤」的流水线，自动生成高质量SFT和RL训练数据，人工标注成本可降低70%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有单图、多图、视频的多模态深度研究任务虽依赖不同的视觉操作，但共享「视觉锚定→外部检索→事实融合」的核心工作流。此前方法未保留从本地化视觉锚点、实体关系、来源支撑事实到答案生成操作的全链路依赖，导致多模态Agent易出现幻觉、证据不可追溯，且无法跨视觉输入类型实现统一训练，不同模态任务需要单独开发模型，复用性差。
### 方法关键点
- 提出**VGEG（Visually Grounded Evidence Graph）**统一结构，关联视觉锚点、真实世界实体、来源可追溯的外部事实、答案生成操作，作为任务构建、过程监督、细粒度评估的统一基准
- 基于VGEG搭建自动化数据引擎，处理单/多图、视频素材，生成110K SFT数据集`OneSearch-VL-SFT-110K`和10K RL数据集`OneSearch-VL-RL-10K`，同时过滤得到高质量专家工具调用轨迹
- 提出**EVGR（Evidence-aware Visual-Grounded Rubric）**奖励函数，从证据可追溯性、视觉锚定准确性两个维度对RL过程进行过程监督，补充传统仅依赖最终答案正确性的奖励缺陷
- 构建操作导向的测试基准`OneSearch-MI-Bench`（多图）和`OneSearch-Video-Bench`（视频），按答案所需的研究操作分类，支持细粒度能力评估
### 关键结果
基于Qwen3-VL-8B初始化训练的OneSearch-VL-8B，在两个新增基准上分别比带工具访问的Qwen3-VL-8B高出20.2、17.6个百分点，在VideoDR基准上高出27.0个百分点，在7个单图VQA基准上平均比基线高出16.3个百分点；消融实验显示，同时混合三种视觉类型数据训练比单类型训练平均提升0.7~4.1个百分点，加入EVGR奖励后比仅用答案+查询奖励的RL方案提升3.8个百分点。
### 核心结论
多模态Agent的训练不能仅优化最终结果正确性，通过结构化的证据依赖设计将过程监督信号落地到视觉锚定、事实溯源的每一个环节，才能同时提升效果和可解释性。
