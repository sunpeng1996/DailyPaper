---
title: Unveiling Spectral Mechanisms in Training-Free LLM Text Detection
title_zh: 揭秘免训练大语言模型文本检测中的谱机制
authors:
- Haitong Luo
- Xuying Meng
- Weiyao Zhang
- Wenji Zou
- Shengfeng Lou
- Xuefeng Jiang
- Chungang Lin
- Yujun Zhang
affiliations:
- Institute of Computing Technology, Chinese Academy of Sciences
arxiv_id: '2608.25944'
url: https://arxiv.org/abs/2608.25944
pdf_url: https://arxiv.org/pdf/2608.25944
published: '2026-08-26'
collected: '2026-08-27'
category: LLM
direction: LLM生成内容检测 · 免训练谱分析
tags:
- LLM-Detection
- Training-Free
- Spectral-Analysis
- Generative-Text
- Frequency-Domain
one_liner: 从理论与实证层面阐释免训练LLM文本检测的谱机制、信号来源及适用边界
practical_value: '- 生成式推荐产出的商品文案、营销话术合规检测可引入谱分析特征，补充传统置信度检测的漏检问题

  - 长文本生成场景（如种草长文、直播脚本）优先采用频域谱检测，短文案/混合编辑内容需结合置信度+波动特征多维度判断

  - UGC与AI生成内容混排的合规审核场景，可按文本长度、连续度分层配置检测策略，降低计算开销'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有免训练LLM文本检测方案多基于置信度类指标，仅统计平均token概率，遗漏了人类写作特有的「生成活力」（信号波动特征）；谱分析虽可捕捉该特征，但内在机制与适用边界尚未明确，落地可靠性不足。
### 方法关键点
从理论与实证双维度拆解谱检测原理，将谱能量与代理LLM输出的对数概率轨迹方差直接关联，解释人类更宽泛的token选择偏好如何形成频域指标可捕捉的波动特征，进一步量化文本长度、采样范围对信号强度的影响。
### 关键结果
长文本、连续约束生成场景下谱检测信号辨识度最高；短文本、碎片化、人机混合编辑场景下仅用频域检测效果下降明显，需结合置信度+波动特征做多维度联合判断。
