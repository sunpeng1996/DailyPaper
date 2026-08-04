---
title: 'StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a Hypergraph
  Field'
title_zh: StyleForge：基于超图场反事实推理的室内家具风格搭配
authors:
- Lingwei Dang
- Shishuo Shang
- Pan Liu
- Jiajia Cheng
- Ziyan Qiu
- Zhenhao Zhang
- Yufei Zhu
- Shenghui Huang
- Qingxin Xiao
- Yun Hao
affiliations:
- School of Software Engineering, South China University of Technology
- School of Information Science and Technology, ShanghaiTech University
arxiv_id: '2608.01954'
url: https://arxiv.org/abs/2608.01954
pdf_url: https://arxiv.org/pdf/2608.01954
published: '2026-08-02'
collected: '2026-08-04'
category: RecSys
direction: 搭配推荐 · 高阶依赖与风格一致性建模
tags:
- Hypergraph
- Counterfactual Reasoning
- Multimodal LLM
- Retrieval
- Style Consistency
one_liner: 提出融合动态超图场与反事实推理的固定布局家具风格搭配框架，性能超现有基线
practical_value: '- 电商家居/服饰套装搭配场景可复用动态超图自适应加权方案，捕捉多商品间高阶风格依赖，解决单品匹配但组合不协调的问题

  - 固定槽位选品场景（如套餐凑单、主题礼包组装）可借鉴反事实替换+马氏距离能量评估方案，快速校验候选的上下文兼容性

  - 推理阶段冻结主模型、仅更新单请求/场景专属候选logits的策略，可大幅降低落地推理延迟，适配个性化实时请求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
固定布局下的家具风格搭配需保留预设的家具品类、位置、朝向、尺寸，现有方案要么独立检索单品类家具，要么依赖静态局部关系建模，组合后极易出现形状、材质、颜色的风格冲突，整体场景一致性差。
### 方法关键点
1. 用冻结多模态大模型提取开放式风格请求与固定布局的结构化风格先验，为每个家具槽位维护可学习候选分布；
2. 动态超图风格场根据目标风格自适应激活、加权布局衍生的超边，精准捕捉多家具间的高阶风格依赖；
3. 采用反事实风格偏好学习，将每个候选视为当前风格场的局部替换，用马氏距离能量评估其上下文兼容性；训练时交替优化风格场与候选logits，推理阶段冻结主模型，仅更新当前房间专属的候选logits，随全局场景上下文演化逐步修正跨槽位风格冲突。
### 关键结果
在3D-FRONT数据集上取得SOTA家具检索效果，场景级风格一致性显著优于单品级、场景级检索基线。
