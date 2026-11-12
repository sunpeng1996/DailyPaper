---
title: 'PolyRoute: A Twelve-Language and Code-Mixed Benchmark for Typed-Decision Routing,
  with Baselines and a Leaderboard'
title_zh: PolyRoute：12语种及语码混合分类决策路由基准数据集（含基线与排行榜）
authors:
- Mohammed Nayeem Khan
- Sarun Kumar K S
affiliations:
- Intel Corporation
arxiv_id: '2611.13843'
url: https://arxiv.org/abs/2611.13843
pdf_url: https://arxiv.org/pdf/2611.13843
published: '2026-11-09'
collected: '2026-11-12'
category: Eval
direction: 多语言分类决策路由基准评估
tags:
- Multilingual Benchmark
- Code-Mixed Text
- Typed-Decision Routing
- Cross-Lingual Transfer
- Leaderboard
one_liner: 发布面向分类决策路由的12语种+语码混合基准数据集、基线系统与公开排行榜
practical_value: '- 跨境电商多语种客服路由场景可直接复用本文三分类路由评估协议，优先上线TF-IDF+逻辑回归基线，成本极低可实现91.9%的准确率

  - 处理Hinglish、Spanglish等语码混合用户输入时，可优先测试英文基座模型，效果略优于通用多语言基座（85% vs 79%）

  - 跨语言模型迭代评估时，可参考本文数据构造逻辑，控制训练测试集5-gram相似度<0.33避免数据泄露，保证评估结果可信度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有分类决策编码器的非英文场景能力缺乏统一评估标准，语码混合、小语种场景的路由效果无从对标

### 方法关键点
1. 发布PolyRoute数据集：含12语种322条原生客服消息、156条语码混合/罗马化消息、967条训练样本，配套三分部路由评估协议
2. 标注采用Qwen3.8-27B双盲标注，保留91%候选，Gemma4-31B独立验证标注一致性达97.2%，训练测试集5-gram相似度最高仅0.33无泄露，所有样本与标注均为LLM生成
3. 完成13个系统的基线测试与排行榜搭建

### 关键结果
通用英文基座路由准确率61.2%，开箱多语言基座77.3%，最优微调模型达96.6%；4个未参与训练的小语种上多语言系统得分77%/90%/93%，语码混合场景英文基座85%略优于多语言基座79%（p=0.134无统计显著性）
