---
title: Improving Proactive AI Assistance with Hierarchical Procedural Understanding
title_zh: 基于层次化流程理解的主动AI助手性能优化方案
authors:
- Jin-Seop Lee
- TaeYeon Won
- SeongJun Jung
- JungHoon Kim
- Boyang Albert Li
- Jin-Young Park
- Jaehong Yoon
- Jee-Hyong Lee
affiliations:
- Sungkyunkwan University
- Nanyang Technological University
arxiv_id: '2610.06505'
url: https://arxiv.org/abs/2610.06505
pdf_url: https://arxiv.org/pdf/2610.06505
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: 主动Agent · 多粒度自适应引导
tags:
- Proactive Agent
- VLM
- Hierarchical Understanding
- Adaptive Guidance
- Multimodal
one_liner: 提出ProactiveCoach套件，支持多粒度自适应主动引导，大幅提升主动AI助手效果
practical_value: '- 电商场景主动导购Agent（直播导购、组装类商品操作指导、AR教程引导）可复用三级粒度（阶段/步骤/动作）引导框架，根据用户熟练度动态切换引导粒度，降低用户操作门槛

  - 训练多粒度任务引导模型时，优先采用分层联合监督方案，相比单粒度监督可提升最高9.6%p的整体性能，无需分别训练多个粒度模型，节省算力与维护成本

  - 自适应引导系统可参考「主模型生成全粒度引导+轻量LLM路由选粒度」的解耦架构，用户切换引导需求时无需重新微调主模型，落地成本极低

  - 流式输入的响应/静默决策场景，可复用论文的正负样本均衡采样策略，解决静默样本占比过高导致的loss偏移问题，提升决策准确率'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有主动AI助手要么仅基于事件检测触发响应，要么仅提供固定粒度的流程引导，无法匹配不同用户的熟练度需求，也难以在流式输入下精准判断引导时机，缺乏适配多粒度引导的训练与评测数据支撑。
### 方法关键点
1. 构建ProactiveCoach-Instruct训练集与ProactiveCoach-Bench评测基准，覆盖7.2K个第一人称流程视频，标注阶段/步骤/动作三级层次化引导内容与触发时机，覆盖组装、烹饪、家居等多场景
2. 提出分层联合监督的VLM微调方法，单个模型同时学习三级粒度的引导内容与触发时机，训练时采用正负样本均衡采样策略解决静默样本过多的loss偏移问题
3. 自适应引导系统采用「主VLM生成全粒度引导+轻量LLM路由选择匹配用户需求的粒度」的解耦架构，无需微调主模型即可切换引导粒度
### 关键结果
1. 相比固定单粒度监督，分层监督在不同VLM骨干上均带来最高9.6%p的整体性能提升
2. 自适应引导系统在四类粒度切换场景下，相比上下文适配基线整体性能提升57.1%p
3. 基于Qwen3-VL-8B微调的模型在所有粒度的引导任务上均显著超越Gemini 3 Flash、GPT-5.4 mini等前沿闭源模型
### 核心结论
主动引导系统的多粒度适配不需要训练多个独立模型，分层联合学习反而能同时提升每个单粒度的引导效果，解耦生成与路由的架构能大幅降低动态适配的落地成本
