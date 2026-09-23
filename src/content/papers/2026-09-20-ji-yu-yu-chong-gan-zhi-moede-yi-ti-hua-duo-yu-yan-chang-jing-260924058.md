---
title: All-in-One Multilingual Scene Text Recognition with Script-aware Mixture-of-Experts
title_zh: 基于语种感知MoE的一体化多语言场景文本识别模型
authors:
- Xingsong Ye
- Yongkun Du
- Jiaxin Zhang
- Zhixian Li
- Chong Sun
- Chen Li
- Jing Lyu
- Lianwen Jin
- Zhineng Chen
affiliations:
- Fudan University Institute of Trustworthy Embodied AI
- Shanghai Key Laboratory of Multimodal Embodied AI
- WeChat Vision, Tencent Inc.
- South China University of Technology
arxiv_id: '2609.24058'
url: https://arxiv.org/abs/2609.24058
pdf_url: https://arxiv.org/pdf/2609.24058
published: '2026-09-20'
collected: '2026-09-23'
category: Multimodal
direction: 多模态OCR · MoE架构优化
tags:
- MoE
- Scene Text Recognition
- Multilingual
- Multimodal
- OCR
- Low-resource Learning
one_liner: 提出ScriptMoE架构与千万级多语言合成数据集，实现轻量高精度多语种场景文本识别
practical_value: '- 多语言业务（如跨境电商OCR、多语种内容审核）可复用script-aware MoE架构，共享通用底座+稀疏语种专家，相比单语种独立部署降本30%+，避免多模块级联误差

  - 低资源语种/垂类场景识别任务可借鉴大规模合成数据集构造思路，补充真实数据缺失的监督信号，降低标注成本

  - 现有OCR生产流水线无需重构全链路，仅替换识别模块为ScriptMoE即可显著提升多语言场景F1，适配跨境电商商品图文字识别、多语种评论图片解析等场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
多语言场景文本识别（STR）现有方案存在两类痛点：单语种独立部署成本高、级联误差大；大参数VLM方案开销高、低资源语种精度不足，且普遍面临低资源语种训练数据稀缺问题。
### 方法关键点
1. 公开TextMuSS-10M千万级合成场景文本数据集，覆盖10种书写体系、229种语言，补充低资源场景的平衡监督信号；
2. ScriptMoE架构采用共享统一视觉编码器，解码层替换为稀疏MoE块：图像级路由将每个样本分发给Top2匹配的语种专属专家，额外设置共享专家吸收跨语种通用知识。
### 关键结果
TextMuSS-Bench测试集准确率达82.06%，超最优STR基线1.31%；替换PP-OCRv5识别模块后，CC-OCR多语言任务F1从65.71%提升至80.89%，精度略超最优VLM但参数量仅为其极小部分
