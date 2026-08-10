---
title: Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection
title_zh: 面向泛化性深度伪造视频检测的多智能体取证推理方法
authors:
- Xuechao Zou
- Shun Zhang
- Kai Li
- Yi Zhou
- Xinyu Sun
- Yuhui Chen
- Zhe Wu
- Congyan Lang
- Junliang Xing
affiliations:
- Beijing Jiaotong University
- Tsinghua University
- Ant Group
arxiv_id: '2608.06865'
url: https://arxiv.org/abs/2608.06865
pdf_url: https://arxiv.org/pdf/2608.06865
published: '2026-08-06'
collected: '2026-08-10'
category: MultiAgent
direction: 多智体协作 · 内容安全检测推理
tags:
- MultiAgent
- Forgery Detection
- Video Forensics
- MLLM
- Dataset
one_liner: 构建覆盖33种生成方式的10万级深度伪造数据集，提出多Agent推理检测框架，效果优于闭源GPT、Gemini
practical_value: '- 内容审核类业务可复用「领域专家Agent+裁判Agent」架构：按违规特征维度（如造假、合规、版权）拆分专用检测Agent，再由裁判Agent对齐输出，降低单模型漏检率

  - 大规模数据集标注可复用多模型聚合+冲突消解pipeline，调用MLLM自动生成细粒度标注，大幅降低人工标注成本

  - 由开源小MLLM组成的多Agent集群可实现优于闭源大模型的效果，适合业务侧降本、数据可控性要求高的场景，无需依赖闭源大模型API'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有深度伪造视频数据集对新型生成方法覆盖不足，且普遍缺少可靠细粒度文本标注；传统单模型/单视角检测方法难以捕捉细微伪造痕迹，对新兴生成方法的泛化性差。
### 方法关键点
1. 发布FaceVid-Forensics-100K数据集：包含10万条视频，覆盖换脸、表情重定向、全脸生成3大类共33种合成方法，配套MLLM自动生成的细粒度视觉观察与取证解释标注
2. 多Agent取证推理框架：4个专属领域专家Agent分别从纹理、光照、运动、物理4个独立视角提取伪造线索，再由裁判Agent整合多份报告输出最终检测结果与解释
### 关键结果
域外测试集上，完全由开源小MLLM组成的框架性能超过所有对比方法，包括闭源GPT、Gemini，在基准所有指标上排名第一。
