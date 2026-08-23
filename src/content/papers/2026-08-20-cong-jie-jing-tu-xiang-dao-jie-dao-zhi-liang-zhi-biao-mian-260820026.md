---
title: 'From Street View Imagery to Street Quality Indicators: Vision Language Inference
  for the Suburban 15-minute City'
title_zh: 从街景图像到街道质量指标：面向郊区15分钟城市的视觉语言推理
authors:
- Joan Perez
- Giovanni Fusco
affiliations:
- Urban Geo Analytics, France
- Université Côte-Azur-CNRS-AMU-Avignon Université, ESPACE, France
arxiv_id: '2608.20026'
url: https://arxiv.org/abs/2608.20026
pdf_url: https://arxiv.org/pdf/2608.20026
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 多模态VLM · 街景图像语义分析
tags:
- VLM
- Multimodal
- Street View Analysis
- Open-source Workflow
- Urban Computing
one_liner: 升级开源SAGAI工作流，支持基于VLM从街景图像大规模评估郊区街道景观质量
practical_value: '- 多VLM共识推理的策略可迁移至多模态内容理解场景（如电商商品图属性打标、UGC内容审核），降低单模型输出的误差

  - 地理一致性视图生成方法可复用在LBS相关推荐（如本地生活到店推荐、商圈选址）的周边环境特征工程环节

  - 模块化、多架构兼容的开源工作流设计思路，可借鉴搭建多模态内容处理的可插拔工程pipeline'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统实地调研评估大范围郊区街景质量耗时耗力，无法支撑15分钟城市规划的大规模分析需求。
### 方法关键点
升级后的开源SAGAI工作流优化了图像采集、地理一致性视图生成能力，支持对接多种VLM架构，采用共识式推理策略，内置集成分析环境，可基于Google街景图像批量提取人行道覆盖率、行人入口密度、植被类型三类步行友好相关的街道质量指标。
### 关键结果
在法国尼斯东北部郊区数千个街景观测点验证，仅少量区域（紧凑型开发区、传统郊区村镇）符合期望的街景质量标准，住宅山地区域指标缺失严重，VLM方案可替代高成本实地调研完成大范围城市诊断。
