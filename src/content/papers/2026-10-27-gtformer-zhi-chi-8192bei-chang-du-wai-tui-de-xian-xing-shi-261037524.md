---
title: 'GTFormer: A Syntax-Free Graph Network Alternative to Transformers for 8192$\times$
  Length Extrapolation in Linear Time'
title_zh: GTFormer：支持8192倍长度外推的线性时间无语法图网络Transformer替代方案
authors:
- Elisabeth Fink
affiliations:
- Middlesex University, Department of Computer Science
arxiv_id: '2610.37524'
url: https://arxiv.org/abs/2610.37524
pdf_url: https://arxiv.org/pdf/2610.37524
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: 长序列建模 · 层级GNN架构优化
tags:
- LongContext
- GNN
- LengthExtrapolation
- LinearScaling
- TransformerAlternative
one_liner: 提出无语法层级GNN架构GTFormer，O(N)复杂度下实现8192倍零样本长序列长度外推
practical_value: '- 长文档RAG场景可复用GTFormer的局部平移边+层级凸门控设计：解决跨chunk的语义绑定问题，避免长文本拆分时的上下文断裂，降低跨chunk召回错误率

  - 超长用户行为/会话序列建模可替换Transformer骨干：O(N)复杂度比RoPE Transformer节省90%以上VRAM，同长度推理latency降低6倍以上，适配高吞吐推荐场景

  - 中小团队落地长上下文能力可借鉴训练范式：仅在≤512长度短序列上训练即可零样本外推到百万级长度，无需昂贵的长序列训练集群成本

  - 无固定语法序列建图可复用无解析层级构图方法：无需依赖外部语法解析器即可自动构建token关联图，适配商品属性关联、用户意图跳转等非结构化序列建模'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer自注意力的O(N²)复杂度限制长序列落地，且短序列训练、长序列部署时会出现注意力稀释、RoPE位置编码漂移问题；现有稀疏注意力、SSM等方案分别存在长距离依赖传播受限、非线性关系建模不足的缺陷，亟需兼顾线性复杂度、强长度外推能力的通用序列建模架构。

### 方法关键点
- 无语法自动构图：将任意token流转为层级多图，由平衡二叉归约树、叶节点局部平移边、层内随机扩展捷径、根到叶广播边四类边构成，节点入度恒≤4，总节点数O(N)
- 凸门控归约机制：自底向上归约时父节点表示为子节点的通道级凸组合，保证激活值始终落在叶节点特征的凸包内，不会随层级深度漂移
- 短序列训练范式：仅用≤512长度的动态生成无重复样本训练，避免模型记忆固定位置特征

### 关键实验
在8个长序列基准（含KV召回、多跳指针、代码scope、多针RAG等）上对比RoPE/正弦位置编码Transformer、纯二叉树GNN等baseline：
- 仅在≤512长度训练的GTFormer零样本外推到4,194,304长度（8192倍），准确率保持98.1%±0.2%，单序列推理耗时796.62ms，峰值VRAM仅22.1GB
- 同长度下比RoPE Transformer推理快6倍，N>16384时Transformer直接OOM，GTFormer仍保持线性内存增长
- 消融实验证实凸门控是长度外推的核心，去掉后准确率跌至<5%，局部平移边可解决二分边界的token拆分问题

### 核心结论
仅靠拓扑归纳偏置（层级凸归约+局部边界绑定）即可实现跨8192倍长度的零样本外推，无需长序列训练、无需修改位置编码，同时兼顾线性复杂度与多跳推理能力
