---
title: 'Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation
  and Editing'
title_zh: Mage-Flow：面向图像生成与编辑的高效原生分辨率基础模型
authors:
- Xinjie Zhang
- Peng Zhang
- Shicheng Zheng
- Jinghao Guo
- Zhaoyang Jia
- Yifei Shen
- Xun Guo
- Yuxuan Luo
- Jiahao Li
- Wenxuan Xie
affiliations:
- Microsoft Mage Team
arxiv_id: '2607.19064'
url: https://arxiv.org/abs/2607.19064
pdf_url: https://arxiv.org/pdf/2607.19064
published: '2026-07-20'
collected: '2026-07-22'
category: Multimodal
direction: 多模态生成 · 文生图与图像编辑优化
tags:
- Diffusion Model
- Text-to-Image
- Image Editing
- VAE
- Efficient Inference
one_liner: 推出4B参数轻量图像生成编辑栈，训练吞吐量提2.5倍，A100上1024分辨率生成仅0.59s
practical_value: '- 电商商品图生成、主图修改场景可直接复用Mage-Flow-Turbo低延迟能力，降低交互式设计响应门槛

  - 多模态生成系统的tokenizer-骨干-系统联合优化思路可迁移到生成式推荐多模态内容生成链路，提升训练推理效率

  - 4步蒸馏+对抗感知引导的低延迟推理方案可复用在搜索推荐实时多模态内容生成（如个性化商品海报）需求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有大规模视觉生成器训练、微调、部署成本高，难以满足交互式高分辨率生成/编辑的落地需求。
### 方法关键点
1. 4B规模生成栈由两个协同设计核心组件构成：轻量高保真潜变量分词器Mage-VAE，采用单步扩散编解码+锚点潜变量正则，分词成本降低1个数量级以上；原生分辨率多模态Diffusion Transformer，基于整流流匹配训练。
2. 结合原生分辨率打包、栈级CUDA kernel fusion，支持灵活分辨率训练。
3. 衍生Base、RL对齐、Turbo三类变体，Turbo版本通过4步蒸馏+对抗感知引导实现低延迟推理。
### 关键结果
端到端训练吞吐量提升约2.5×；单张A100上1024²分辨率下，Turbo版生成耗时0.59s、编辑耗时1.02s，内存占用低，基准测试性能持平主流大模型
