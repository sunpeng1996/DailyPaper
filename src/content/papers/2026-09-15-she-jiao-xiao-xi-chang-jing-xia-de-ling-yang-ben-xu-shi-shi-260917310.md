---
title: Zero-shot narrative detection in social messaging
title_zh: 社交消息场景下的零样本叙事识别
authors:
- Jesús M. Fraile-Hernández
- Anselmo Peñas
- Patrick Giedemann
affiliations:
- Universidad Nacional de Educación a Distancia
- Zurich University of Applied Sciences
arxiv_id: '2609.17310'
url: https://arxiv.org/abs/2609.17310
pdf_url: https://arxiv.org/pdf/2609.17310
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: 大语言模型 · 零样本文本分类
tags:
- Zero-shot
- Narrative Detection
- LLM
- Prompt Engineering
- Ensemble Learning
one_liner: 验证LLM零样本识别社交消息隐藏叙事能力，搭配人工描述+多数投票可媲美监督系统
practical_value: '- 零样本分类场景优先采用人工撰写的类别语义描述作为prompt，不要盲目使用few-shot或自动生成的描述，避免框架偏移导致精度下降

  - 无标注数据的新领域分类任务，可搭配简单的多数投票集成策略，低成本提升系统鲁棒性与整体精度

  - 资源受限场景下优先选型中等尺寸LLM，可在保证效果稳定性的同时降低推理成本，不需要盲目追求大参数模型'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统社交叙事识别依赖监督模型，大量新兴领域无标注数据可用，且浅层情感/主题分析无法捕捉深层策略性叙事意图，需要低成本可扩展的零样本方案。
### 方法关键点
在Dipromats、SemEval两个数据集上系统对比三类prompt策略（人工撰写叙事描述、自动生成描述、仅用类别标题）、few-shot、多数投票集成策略的效果，同时测试不同尺寸LLM的性能与prompt鲁棒性。
### 关键结果
人工撰写描述的零样本方案精度显著优于自动生成描述/few-shot方案，后者因框架偏移常导致精度下降10%以上；结合多数投票集成后，零样本方案可媲美监督系统效果；大模型性能最优，prompt敏感度比中小模型低20%，中等尺寸模型可平衡效果与推理成本。
