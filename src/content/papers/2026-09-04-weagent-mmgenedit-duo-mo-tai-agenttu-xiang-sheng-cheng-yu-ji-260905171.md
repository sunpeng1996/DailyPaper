---
title: 'WeAgent-MMGenEdit: A Full-Stack Recipe for Multimodal Agentic Image Generation
  and Editing'
title_zh: WeAgent-MMGenEdit：多模态Agent图像生成与编辑全栈方案
authors:
- Hui Zhang
- Zongkai Liu
- Liqiang Niu
- Juntao Liu
- Han Li
- Zhen Cao
- Wenchao Chen
- Chengduo Zhao
- Fandong Meng
affiliations:
- Weixin AI, Tencent
arxiv_id: '2609.05171'
url: https://arxiv.org/abs/2609.05171
pdf_url: https://arxiv.org/pdf/2609.05171
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: 多模态Agent · 图像生成与编辑优化
tags:
- Multimodal Agent
- Image Generation
- Image Editing
- SFT
- Reinforcement Learning
- Tool Use
one_liner: 提出全栈多模态Agent图像生成编辑方案，3B激活参数量性能逼近万亿参数大模型
practical_value: '- 多模态Agent的检索-验证-整合工具链设计可直接复用在电商商品图智能生成、营销海报知识对齐场景，解决生成内容事实错误、实体与属性绑定混乱问题

  - 三层可验证Checklist设计可迁移到Agent训练数据标注与效果评估，尤其是需要多跳检索、跨模态信息对齐的生成类业务任务

  - 策略与图像生成后端分离的异步RL训练框架可降低多模态Agent训练成本，避免后端渲染波动影响策略优化效果

  - 多参考图像编辑的LoRA微调方案可直接用在电商商品图批量编辑、海报模板智能替换场景，提升多源参考素材的融合准确度'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有图像生成/编辑模型依赖参数内存储的知识，处理需要外部实时/长尾知识的任务（如信息图更新、赛事海报生成、商品图事实对齐）时事实幻觉严重；现有Agent式生成方案存在视觉证据验证不足、单策略负载过载、实体-属性-布局跨模态绑定弱三大问题，且缺乏针对多图像编辑的基准与标准化训练流程，无法满足业务场景对生成内容事实准确性的要求。
### 方法关键点
- 设计WeAgent-Harness多模态运行时，实现Retrieve-Verify-Integrate-Deliver专用工具链，带持久化多模态证据存储，将验证后的证据渲染为带显式实体-属性-布局绑定的 dense carrier，避免策略上下文过载
- 构建包含23K条SFT轨迹、14.7K条RL任务的WeDataset-MMGenEdit，配套300个人工审核的中英双语基准WeBench-MMGenEdit，采用Agent流程、生成输入、输出图像三层独立评估机制
- 双阶段后训练流程：Agent侧先做SFT对齐工具调用协议，再基于Checklist做RL优化证据获取与整合质量；图像编辑侧先做多参考SFT适配异质参考输入，再做多目标RL优化生成事实准确性
### 关键结果
在WeBench-MMGenEdit上对比GPT-Image-2、Gemini3.1-Flash、开源Agent生成系统等基线，总参数30B/激活参3B的WeAgent-RL搭配WeEdit-M-RL，生成任务加权平均分比GPT-Image-2高25.9%，编辑任务高22.8%，性能接近万亿参数Agent，仅用其3%的参数量。
### 核心洞见
多模态知识密集型生成任务的核心瓶颈不是生成能力，而是证据的可靠获取、验证与结构化传递效率
